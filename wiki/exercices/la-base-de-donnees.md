# Exercice 8 : La base de données

Vous allez maintenant ajouter une base de données à votre [application d'objets connectés](objets-connectes-interface.md).

1. Créez les classes qui représentent les tables de la base de données.
    1. La base de données devra avoir au minimum une table pour les objets connectés et une autre pour stocker l'historique (valeurs captées par ces objets ainsi que date et heure de la captation). Une valeur captée peut être une température, un taux d'humidité, une présence détectée, une lumière à l'état allumé, une prise de courant à l'état éteint, etc.
    2. La dernière valeur captée est considérée comme la valeur actuelle de l'objet connecté.
    3. Vous devez coder les classes mais pas créer physiquement la base de données puisqu'elle sera créée automatiquement plus loin.
    4. Pour faciliter votre travail, ne lancez pas l'application dans le simulateur tant que ça ne vous sera pas demandé.
2. Configurez votre application pour qu'elle puisse travailler avec cette base de données.
3. Faites le nécessaire pour que l'application contienne quelques données initiales.
4. Dans le `ContentView`, faites afficher la liste d'objets connectés à partir de la base de données.
    1. Pour l'instant, ne vous souciez pas de faire afficher la valeur actuelle de chaque objet à partir de la base de données. Vous pouvez coder cette information en dur.
    2. Vous pouvez mettre en commentaire les autres informations que vous aviez codées en dur afin de ne pas oublier le design de votre vue.
    3. N'oubliez pas : comme toujours, le code doit informer l'usager correctement si aucune donnée n'était présente dans la base de données. Ici, vous devez utiliser un `ContentUnavailableView`.
    4. Avez-vous pensé à trier vos données, tel qu'exigé pour toute application qui affiche une liste d'informations?
5. Lancez maintenant l'application dans le simulateur (et non pas dans la prévisualisation). Ceci créera physiquement la base de données, à condition que vous ayez correctement configuré l'application.
6. Installez sur votre Mac un outil de votre choix pour éditer une base de données SQLite.
7. Retrouvez les fichiers de la base de données sur le disque de votre ordinateur. Ouvrez la base de données dans votre éditeur SQLite et constatez la présence des données initiales. Assurez-vous que les clés étrangères soient bien remplies.
8. À partir du Finder, créez un dossier `dev` sous le dossier de l'application. Ce dossier ne doit pas faire partie du projet donc il ne sera pas visible dans Xcode.
9. Faites une impression d'écran de la structure de la base de données à partir de votre éditeur SQLite. Notez que certains outils n'offrent pas cette fonctionnalité. Ce type de manipulation pourrait être demandé en examen.
10. Placez cette image dans le dossier `dev`.
