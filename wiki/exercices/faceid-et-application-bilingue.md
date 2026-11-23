# Exercice 18 : FaceID et application bilingue

1. Téléchargez l'application Sudoku ici : <https://github.com/ZacharyBeshara/SudokuUI>
    1. Modifiez cette application afin qu'elle utilise [Face ID](../lecons/l-authentification.md) pour vous authentifier (bon, elle ne manipule pas d'informations sensibles mais ça permet de pratiquer la fonctionnalité 😉).

        !!! Warning "Attention"
            Le code cible iOS < 17 donc vous devrez modifier le `@Observable` pour utiliser [l'ancienne syntaxe](../complements/fonctions-obsoletes-ou-anciennes-syntaxes.md).

    2. Testez bien votre application pour vous assurer qu'elle réagisse comme il faut dans toutes ces situations :
        1. La connexion avec Face ID est réussie
        2. Face ID ne reconnaît pas votre visage
        3. Face ID est désactivé et le mot de passe entré est bon
        4. Face ID est désactivé et le mot de passe entré n'est pas bon
        5. L'authentification n'a pas été complétée après 5 minutes

        Notez que si l'application affiche un `ProgressView` après le processus d'authentification, c'est que vous n'avez pas correctement déclaré la variable de type `Authentification` (la déclaration nécessite quelque chose de particulier avec l'ancienne syntaxe pour les variables observables).

    3. Faites le nécessaire pour que chaque chaîne affichée à l'écran puisse apparaître en anglais ou en français selon la configuration du simulateur. Suggestion : utilisez l'IA pour vous aider à traduire les chaînes.
2. Ouvrez l'application GuessTheFlag dans Xcode. Si vous ne l'avez pas faite dans l'[exercice sur la correction de code](applications-a-corriger.md), voici le lien vers une [version fonctionnelle du projet](https://github.com/twostraws/HackingWithSwift/tree/3eeaa4eca7ee0782e9bcb9101c66a5870947410f/SwiftUI/project15/FixedProjects/project2).
    1. Faites la [localisation](../lecons/la-localisation-traduction.md) de l'application GuessTheFlag et assurez-vous que les chaînes apparaissent dans la langue utilisée par le simulateur. L'application doit fonctionner en anglais et en français.
3. **OPTIONNEL** : ajoutez l'authentification et la localisation à votre application d'objets connectés.
