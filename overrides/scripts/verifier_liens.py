"""Vérifie que les liens externes (http/https) des fichiers Markdown sont toujours valides.

Utilisation :
    python overrides/scripts/verifier_liens.py                 # analyse wiki/
    python overrides/scripts/verifier_liens.py wiki/lecons     # un dossier précis
    python overrides/scripts/verifier_liens.py --redirections  # affiche aussi les redirections

Code de sortie : 0 si tous les liens sont valides, 1 sinon.
N'utilise que la bibliothèque standard.
"""

import argparse
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# URL brute ou autolien <url> : s'arrête aux espaces et aux délimiteurs Markdown/HTML courants,
# mais conserve les parenthèses équilibrées (ex. « allsatisfy(_:) » dans la doc d'Apple).
URL_RE = re.compile(r"https?://(?:[^\s<>\"'`\]()]|\([^\s<>()]*\))+")
# Lien Markdown [texte](url "titre") : capture l'URL complète, parenthèses équilibrées incluses.
MD_LINK_RE = re.compile(r"\]\((https?://(?:[^\s()]|\([^\s()]*\))+)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")

# Domaines fictifs utilisés comme exemples ou espaces réservés dans les notes (jamais de vrais liens).
DOMAINES_IGNORES = {"localhost", "127.0.0.1", "0.0.0.0", "mondomaine.com", "votredomaine.com", "domaine.com"}
# Domaines réservés aux exemples (RFC 2606 / 6761) : example.com, monsite.test, etc.
SUFFIXES_IGNORES = ("example.com", "example.org", "example.net", ".example", ".test", ".invalid", ".local")


def est_lien_reel(url: str) -> bool:
    """Écarte les espaces réservés : schéma seul (« http:// »), hôte sans domaine, domaines d'exemple."""
    hote = (urllib.parse.urlsplit(url).hostname or "").lower()
    if "." not in hote or hote.startswith("www.") and hote[4:] in DOMAINES_IGNORES:
        return False
    return hote not in DOMAINES_IGNORES and not hote.endswith(SUFFIXES_IGNORES)

ENTETES = {
    # Plusieurs sites refusent les requêtes sans User-Agent de navigateur.
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "fr,en;q=0.8",
}
# À l'inverse, certains sites (ex. uuidgenerator.net) coupent la connexion quand un client se dit
# Chrome sans en avoir l'empreinte TLS : on réessaie alors avec un User-Agent honnête.
ENTETES_SIMPLES = {"User-Agent": "verifier-liens/1.0 (Python urllib)"}


def extraire_liens(fichier: Path, inclure_code: bool):
    """Retourne une liste de (url, numéro de ligne)."""
    liens = []
    dans_bloc_code = False
    for no, ligne in enumerate(fichier.read_text(encoding="utf-8").splitlines(), start=1):
        if FENCE_RE.match(ligne):
            dans_bloc_code = not dans_bloc_code
            continue
        if dans_bloc_code and not inclure_code:
            continue
        if not inclure_code:
            ligne = INLINE_CODE_RE.sub("", ligne)

        trouves = set(MD_LINK_RE.findall(ligne))
        for url in URL_RE.findall(ligne):
            # Ignore les URL brutes déjà couvertes (tronquées) par un lien Markdown.
            if not any(t.startswith(url) for t in trouves):
                trouves.add(url.rstrip(".,;:!?*_"))
        for url in trouves:
            if est_lien_reel(url):
                liens.append((url, no))
    return liens


# github.com/<proprio>/<dépôt>/blob/<branche>/<chemin> : GitHub répond 503/429 aux clients qui ne
# sont pas de vrais navigateurs. On vérifie plutôt le fichier sur raw.githubusercontent.com.
GITHUB_BLOB_RE = re.compile(r"^https://github\.com/([^/]+/[^/]+)/blob/(.+)$")


def url_a_verifier(url: str) -> str:
    url = url.split("#", 1)[0]  # le fragment n'est jamais envoyé au serveur
    return GITHUB_BLOB_RE.sub(r"https://raw.githubusercontent.com/\1/\2", url)


def verifier(url: str, delai: float):
    """Retourne (statut, url finale ou message d'erreur)."""
    url_requete = url_a_verifier(url)
    contexte = ssl.create_default_context()
    derniere_erreur = None
    for methode, entetes in (("HEAD", ENTETES), ("GET", ENTETES), ("GET", ENTETES_SIMPLES)):
        requete = urllib.request.Request(url_requete, headers=entetes, method=methode)
        try:
            with urllib.request.urlopen(requete, timeout=delai, context=contexte) as rep:
                return rep.status, rep.geturl()
        except urllib.error.HTTPError as e:
            derniere_erreur = (e.code, e.reason)
            # Certains serveurs refusent HEAD : on réessaie en GET.
            if methode == "HEAD" and e.code in (400, 403, 404, 405, 406, 429, 500, 501, 503):
                continue
            return e.code, str(e.reason)
        except Exception as e:  # DNS, SSL, délai dépassé, connexion refusée...
            derniere_erreur = (None, f"{type(e).__name__}: {getattr(e, 'reason', e)}")
            # Connexion coupée : on réessaie (GET, puis User-Agent simple).
            if entetes is ENTETES:
                continue
    return derniere_erreur


def est_ignore(statut, info: str) -> bool:
    """Résultats non concluants qu'on ne signale pas comme liens brisés.

    - 403 : souvent une protection anti-robot (Cloudflare, etc.), le lien fonctionne dans un navigateur.
    - 429 : « Too Many Requests », renvoyé par certaines protections anti-robot (ex. sentinelone.com)
      aux clients qui ne sont pas de vrais navigateurs, même à la première requête.
    - CERTIFICATE_VERIFY_FAILED : chaîne de certificats incomplète côté serveur ou magasin local
      de certificats Python incomplet (fréquent sur macOS).
    """
    return statut in (403, 429) or "CERTIFICATE_VERIFY_FAILED" in str(info)


def main():
    parser = argparse.ArgumentParser(description="Vérifie les liens externes des fichiers Markdown.")
    parser.add_argument("chemins", nargs="*", default=["wiki"], help="Dossiers ou fichiers .md (défaut : wiki)")
    parser.add_argument("--delai", type=float, default=15, help="Délai d'attente par requête en secondes (défaut : 15)")
    parser.add_argument("--fils", type=int, default=16, help="Nombre de requêtes simultanées (défaut : 16)")
    parser.add_argument("--inclure-code", action="store_true", help="Vérifie aussi les URL dans les blocs de code")
    parser.add_argument("--redirections", action="store_true", help="Affiche les liens redirigés vers une autre URL")
    args = parser.parse_args()

    fichiers = []
    for chemin in map(Path, args.chemins):
        fichiers += sorted(chemin.rglob("*.md")) if chemin.is_dir() else [chemin]

    occurrences = defaultdict(list)  # url -> [(fichier, ligne)]
    for f in fichiers:
        for url, no in extraire_liens(f, args.inclure_code):
            occurrences[url].append((f, no))

    print(f"{len(occurrences)} liens uniques dans {len(fichiers)} fichiers. Vérification...\n", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=args.fils) as ex:
        resultats = dict(zip(occurrences, ex.map(lambda u: verifier(u, args.delai), occurrences)))

    brises, rediriges, ignores = [], [], 0
    for url, (statut, info) in sorted(resultats.items()):
        if est_ignore(statut, info):
            ignores += 1
        elif statut is None or statut >= 400:
            brises.append((url, statut, info))
        elif args.redirections and info.rstrip("/") != url_a_verifier(url).rstrip("/"):
            rediriges.append((url, statut, info))

    def afficher(url, detail):
        print(f"  {url}\n      -> {detail}")
        for f, no in occurrences[url]:
            print(f"      {f}:{no}")

    if rediriges:
        print(f"=== {len(rediriges)} lien(s) redirigé(s) ===")
        for url, _, finale in rediriges:
            afficher(url, finale)
        print()

    if ignores:
        print(f"{ignores} lien(s) ignoré(s) (403, 429 ou certificat SSL non vérifiable).\n", file=sys.stderr)

    if brises:
        print(f"=== {len(brises)} lien(s) brisé(s) ===")
        for url, statut, info in brises:
            afficher(url, f"{statut or 'ERREUR'} {info}")
    else:
        print("Tous les liens sont valides.")

    sys.exit(1 if brises else 0)


if __name__ == "__main__":
    main()
