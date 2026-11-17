# Exercice 5 : Jeu de mémoire

Vous devez créer une nouvelle application pour iPhone en SwiftUI. Il s'agit d'un jeu de mémoire.

!!! Note
    Je vous conseille de ne pas utiliser l'intelligence artificielle dans cet exercice, sauf peut-être pour lui demander des explications sur un concept ou pour vous assister dans l'interface utilisateur. Gardez en tête que vous ne pourrez pas vous fier sur l'IA pour vous aider pendant les examens.

Le jeu consiste en un tableau de cartes face cachée. Chaque carte comporte un symbole de votre choix tiré de la banque de symboles SF. Le joueur doit retourner les cartes deux à deux afin de trouver les paires.

Après chaque essai, les cartes sont retournées face cachée sauf si une paire a été trouvée.

Le jeu se termine quand toutes les paires ont été trouvées.

1. Modélisez vos données afin de pouvoir retenir les informations sur une carte : son symbole, sa couleur et son état (face cachée ou visible). Notez que vous pourriez avoir besoin d'autres informations pour réaliser cet exercice. Si c'est le cas pour vous, vous les ajouterez le moment venu.
2. Lors du démarrage de l'application, le jeu est généré automatiquement afin que 6 cartes apparaissent face cachée. Les cartes doivent être identiques deux à deux (même symbole et même couleur) et leur position doit être donnée au hasard.
3. En tout temps, la vue affichera toutes les cartes. À vous de déterminer la meilleure disposition.
4. Un clic sur une carte retournera la carte afin qu'on voie son symbole. L'usager devra retourner exactement deux cartes. Si les deux cartes ont le même symbole, un message indiquera que l'usager a réussi et les cartes demeureront visibles. Sinon, un message indiquera que l'usager doit recommencer. À vous de déterminer ce qui fera en sorte que les deux cartes soient remises face cachée.
5. Si vous avez déclaré des fonctions, assurez-vous qu'elles soient correctement documentées.
6. Prenez soin d'ajouter un AppIcon et d'ajuster le nom qui apparaît sous cette icône.
7. Quand tout est fonctionnel, installez l'application sur un iPhone.

*Idée de base suggérée par ChatGPT.*
