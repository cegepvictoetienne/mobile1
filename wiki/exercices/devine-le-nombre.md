# Exercice 3 : Devine le nombre

Dans cet exercice et dans le suivant, vous allez créer un petit jeu qui consiste à deviner un nombre généré au hasard.

!!! Note
    Je vous conseille de ne pas utiliser l'intelligence artificielle dans cet exercice, sauf peut-être pour lui demander des explications sur un concept.

1. Créez un projet SwiftUI pour iOS.
2. Commencez par générer l'écran :
    1. Un texte invitera l'usager à deviner le nombre.
    2. Une case de saisie permettra à l'usager d'entrer un nombre. Le clavier qui apparaît ne doit permettre que l'entrée de nombres.
    3. Un bouton permettra de valider le nombre. Vous coderez son traitement au prochain numéro.
    4. L'application doit pouvoir afficher un message à l'usager.
3. Un peu de logique maintenant :
    1. Votre application aura besoin d'une variable d'état qui contient un nombre généré au hasard entre 1 et 100 inclusivement.
    2. Quand le bouton de soumission sera cliqué, l'application vérifiera si le nombre entré est égal à celui qu'il fallait deviner, s'il est plus petit ou s'il est plus grand.
    3. L'application doit afficher à l'usager « Bravo! », « Trop petit » ou « Trop grand ». À vous de déterminer la logique pour que le message apparaisse correctement. Rappel : il n'est pas possible d'ajouter une vue dans le code de traitement du bouton.
    4. Si l'usager a entré autre chose qu'un nombre, il doit être avisé que seuls les nombres sont permis. Notez qu'avec le clavier du simulateur, vous ne pourrez entrer que des nombres mais si le simulateur permet l'utilisation du clavier physique, vous pourrez entrer autre chose.
4. Prenez le temps de soigner votre écran : alignements, espacements, apparence du `TextField`, apparence du bouton.
5. Testez votre application dans le simulateur en désactivant le clavier physique.
6. **OPTIONNEL** : Une fois que votre application fonctionne bien, apportez-y quelques bonifications.
    1. D'abord, dans le cas où le nombre est trop petit, la bordure du `TextField` doit être bleue.
    2. Quand il est trop grand, elle doit être orangée.
    3. Dans le cas où ce n'est pas un nombre, elle doit être rouge.
    4. Dès que l'usager commence à modifier le texte dans le `TextField`, le message doit être remis à blanc et la bordure du `TextField` doit redevenir à sa couleur de départ.
    5. Astuce : pour ne pas que le contenu de l'écran bouge verticalement quand le message apparaît ou disparaît, forcez sa hauteur à l'aide de `.frame(height: 50)`.

*Idée de base suggérée par ChatGPT.*
