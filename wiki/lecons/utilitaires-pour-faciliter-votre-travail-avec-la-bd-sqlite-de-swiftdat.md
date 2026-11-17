# Utilitaires pour faciliter votre travail avec la BD SQLite de SwiftData

## Copier les BD SwiftData à l'aide de copier_default_store.py

Le chemin de la base de données SQLite générée par SwiftData dans le simulateur est plutôt complexe :

`/Users/monnom/Library/Developer/CoreSimulator/Devices/[UDID]/data/Containers/Data/Application/[app GUID]/Library/Application Support/default.store`

De plus, le app GUID change à chaque fois que l'application est exécutée.

Pourtant, lors du développement de l'application, il est souvent requis de consulter les données de la BD afin de s'assurer que l'application fait bien son travail.

J'ai donc écrit un petit script Python qui se charge de copier sur le bureau toutes les bases de données SwiftData présentes dans le simulateur.

Vous pouvez adapter le script si vous désirez effectuer la copie à un autre endroit.

Vous devez sans faute ajuster le nom des dossiers pour qu'ils utilisent votre nom d'utilisateur.

Les instructions pour exécuter le fichier sont fournies dans le commentaire d'en-tête.

```python title="Python"
#!/usr/bin/env python3

"""
Copie tous les fichiers du simulateur dont le nom débute par default.store (ex : default.store, default.store-shm et default.store-wal) dans un dossier plus facile à atteindre.
N'écrase pas les fichiers existants. Ajoute plutôt un nombre à la fin du fichier pour le rendre unique (ex : default1.store).
Utilisation : python3 copier_default_store.py
Programmé par Christiane Lagacé : https://christianelagace.com
Le 22 avril 2024
Dernière modification par Christiane Lagacé
Le 27 janvier 2026
"""

import os, shutil

# Constantes

DEBUT_FICHIER = 'default.store'
DOSSIER_SOURCE = '/Users/monnom/Library/Developer/CoreSimulator/Devices'
DOSSIER_CIBLE = '/Users/monnom/Desktop/BD'

def creer_dossier_cible_si_inexistant():
    """
        Crée le dossier cible s'il n'existe pas.
    """
    if not os.path.exists(DOSSIER_CIBLE):
        print(f"Création du dossier {DOSSIER_CIBLE}")
        os.makedirs(DOSSIER_CIBLE)

def nom_unique(fichier):
    """
        Ajoute un nombre à la fin du nom d'un fichier afin de le rendre unique dans le dossier cible.

        Paramètres
        ----------
        fichier : str
            Nom du fichier sans le chemin, avec l'extension (ex : default.store)

        Retour
        ------
        nouveau_fichier : str
            Nom du fichier original si était unique, ou additionné d'un nombre s'il ne l'était pas (ex : default1.store).
    """
    nombre = 1
    nouveau_fichier = fichier
    debut = os.path.splitext(fichier)[0]
    extension = os.path.splitext(fichier)[1]

    while os.path.exists(os.path.join(DOSSIER_CIBLE, nouveau_fichier)):
        nouveau_fichier = debut + str(nombre) + extension
        nombre += 1

    return nouveau_fichier;

def main():
    """
        Procédure principale
    """

    creer_dossier_cible_si_inexistant()

    print(f'Recherche des fichiers qui débutent par {DEBUT_FICHIER} dans le dossier {DOSSIER_SOURCE}.')

    fichiers = []

    for root, dirs, files in os.walk(DOSSIER_SOURCE):
         for file in files:
            if file.startswith(DEBUT_FICHIER):
                fichiers.append(os.path.join(root, file))

    if len(fichiers) > 0:
         print("Fichiers trouvés :")

        try:
             for index, fichier in enumerate(fichiers):
                 print(f'[{index + 1}] {fichier}')
                 shutil.copy(fichier, DOSSIER_CIBLE + '/' + nom_unique(os.path.basename(fichier)))
                 print('Copie réussie!')

             print("***")
             print(f"Les fichiers ont été copiés dans le dossier {DOSSIER_CIBLE}.")
             print("***")

         except Exception as e:
             print(f"Un problème a été rencontré lors de la copie du fichier : {e}")
    else:
         print("***")
         print("Aucun fichier trouvé.")
         print("***")

if __name__ == "__main__":
    main()
```

Attention : ce script copiera également les fichiers `default.store` et `default.store.*` situés dans un dossier au format `/Users/monnom/Library/Developer/CoreSimulator/Devices/[UDID]/data/Library/Application Support` (notez la fin du chemin qui est différente, notamment par l'absence du [app GUID]).

Cette base de données fait partie de l'implémentation interne de SwiftData. Elle ne contient pas les tables liées à vos modèles.

À vous de travailler avec la bonne base de données.

## Supprimer les BD SwiftData à l'aide de supprimer_default_store.py

Dans une application SwiftUI avec SwiftData, la base de données et ses données initiales sont créées automatiquement à condition que la base de données n'existe pas déjà.

Pendant la phase de développement, lorsque vous modifiez la structure de la base de données ou encore les données initiales, le plus simple est de supprimer la base de données qui existe dans le simulateur.

J'ai écrit un script Python qui se charge de supprimer toutes les bases de données SwiftData présentes dans le simulateur.

Attention : ce script supprimera TOUTES les bases de données générées dans le simulateur de Xcode.

Vous devez sans faute ajuster le nom du dossier source pour qu'il utilise votre nom d'utilisateur.

Les instructions d'exécution sont précisées dans le commentaire d'en-tête.

```python title="Python"
#!/usr/bin/env python3

"""
# Supprime tous les fichiers dont le nom débute par default.store (ex : default.store, default.store-shm et default.store-wal).
# Utilisation : python3 supprimer_default_store.py
# Programmé par Christiane Lagacé : https://christianelagace.com
# Le 22 avril 2024
# Dernière modification par Christiane Lagacé
# Le 27 janvier 2026
"""

import os

# Constantes

DEBUT_FICHIER = 'default.store'
DOSSIER_SOURCE = '/Users/monnom/Library/Developer/CoreSimulator/Devices'

def main():
    """
    Procédure principale
    """

    print(f'Recherche des fichiers qui débutent par {DEBUT_FICHIER} dans le dossier {DOSSIER_SOURCE}.')

    fichiers = []

    for root, dirs, files in os.walk(DOSSIER_SOURCE):
        for file in files:
             if file.startswith(DEBUT_FICHIER):
                 fichiers.append(os.path.join(root, file))

    if len(fichiers) > 0:
        try:
             for index, fichier in enumerate(fichiers):
                 print(f'[{index + 1}] {fichier}')
                 os.remove(fichier)
                 print('* Suppression réussie! *')

         except Exception as e:
            print(f"Un problème a été rencontré lors de la suppression du fichier : {e}")
    else:
         print("***")
         print("Aucun fichier trouvé.")
         print("***")

if __name__ == "__main__":
    main()
```
