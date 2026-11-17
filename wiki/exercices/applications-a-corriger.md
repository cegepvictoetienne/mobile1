# Exercice 17 : Applications à corriger

Un bon développeur doit être habile à trouver les erreurs dans un programme.

Je vous présente ici quelques applications SwiftUI qui ne compilent pas, ne font pas bien leur travail ou nécessitent un ajout de fonctionnalité. Vous devez rendre chacune de ces applications fonctionnelle.

1. L'application [GuessTheFlag](../fichiers/GuessTheFlag-main.zip) est un petit jeu qui demande de deviner le drapeau d'un pays parmi trois images.
    1. Elle ne compile pas alors vous allez devoir la réparer.
    2. Une fois réparée, les joueurs se plaignent que le jeu commence souvent par le même pays. Ajustez l'application pour que les pays soient mieux mélangés.
    3. Assurez-vous que des drapeaux grisés apparaissent seulement lorsque la bonne réponse est affichée.
2. L'application [MonAgent](../fichiers/MonAgent.zip) permet de converser avec un agent d'IA ([Cohere](https://cohere.com/fr) a été utilisé parce qu'il permet de tester sans devoir payer). Par contre, elle ne fonctionne pas du tout.
    1. Créez-vous une clé d'API et inscrivez-la à l'endroit approprié (les instructions sont dans un des fichiers de l'app!).
    2. Corrigez les erreurs pour rendre l'application fonctionnelle.
    3. Faites le nécessaire pour que le `#Preview` affiche quelques messages de la part de l'IA et de l'usager.