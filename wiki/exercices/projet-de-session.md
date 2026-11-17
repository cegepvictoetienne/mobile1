# Projet de session

Le projet de session constitue l'épreuve finale de ce cours. Il sera réalisé en classe et hors classe pendant les 3 à 5 dernières semaines de la session.

Il s'agit de projets individuels.

Le projet compte pour **50 % de la note finale**.

Les détails du projet de session vous sont présentés dès maintenant afin que vous puissiez commencer à réfléchir à votre sujet.

## Consignes

Vous devez développer une application pour iPhone qui répond aux critères suivants :

1. L'application doit être codée en SwiftUI avec [SwiftData](../lecons/swiftdata.md).
2. Le sujet doit être acceptable dans le contexte d'une maison d'enseignement et il doit susciter de l'intérêt. Votre prof prendra en note le sujet que vous avez choisi.
3. Tout extrait de code inspiré du Web ou de l'IA doit être correctement identifié (mention **Code emprunté** ou **Code emprunté inspiré de** suivie de l'URL ou du nom de l'IA, avec la date). Si le code emprunté fait plus d'une ligne, la fin doit être identifiée par **Fin du code emprunté**. Une source non citée est considérée comme du plagiat.
4. Le prof peut vous questionner sur votre code, soyez préparés à justifier vos choix et à expliquer ce que le code fait.
5. Le nom du dossier du projet doit être au format `nomprenom-projetsession`.
6. Le titre de l'application doit être votre nom et il doit apparaître dans la barre de navigation de l'écran principal.
7. L'application doit être en français (langue par défaut, commentaires, documentation).
8. Le texte qui ne provient pas de la base de données doit être correctement [localisé](../lecons/la-localisation-traduction.md) (français-anglais).
9. Il doit y avoir un [AppIcon](../lecons/l-appicon.md).
10. L'application doit utiliser au moins un [capteur](../lecons/les-capteurs.md). Les informations captées doivent être en lien direct avec l'application. Si vous choisissez un capteur qui a déjà été utilisé en exercice (ex : Attitude), vous devez aller plus loin que ce qui a été fait en exercice.
11. Il doit y avoir [plusieurs écrans](../lecons/les-applications-multivues.md) dans l'application dont un qui affiche une liste cliquable, un qui affiche le détail d'un élément de la liste grâce à un ou plusieurs paramètres et au moins un autre écran.
12. Dans la barre de navigation, il doit y avoir un [menu](../lecons/le-menu.md) dans lequel on peut cliquer sur un mot ou sur une icône pour faire dérouler une liste d'options. Le rôle de chaque option du menu est à votre choix et le tout doit être fonctionnel (contrairement à l'exercice sur les objets connectés dans lequel la fonctionnalité était optionnelle).
13. L'interface graphique doit utiliser au moins une [image](../lecons/les-images-et-icones.md). Elle peut avoir été ajoutée dans les ressources de l'application ou être appelée via son URL. Les icônes ne sont pas considérées comme des images.
14. L'application doit travailler avec une base de données SQLite dans laquelle l'application se charge d'insérer des données initiales.
15. La base de données doit contenir au moins deux tables liées par une relation de 1 à plusieurs.
16. L'application doit effectuer toutes les [opérations CRUD](../lecons/crud-avec-swiftdata.md) (*Create, Read, Update, Delete* ou, si vous préférez, `INSERT`, `SELECT`, `UPDATE` et `DELETE`) sur les données SQLite.
17. Il doit y avoir une confirmation avant suppression.
18. L'application doit faire appel à un service Web. Vous avez le choix :
    1. **Service qui fait la synchronisation des données dans une base de données MySQL**
        1. Il doit y avoir une fonctionnalité de votre application qui appelle le service Web pour effectuer une [synchronisation des données](../lecons/synchronisation-des-donnees-locales-dans-le-nuage.md) dans une base de données MySQL. Il faut tenir compte des ajouts, des modifications et des suppressions (dans un sens seulement, pour une seule table).
        2. L'usager doit être informé de la réussite ou non de la synchronisation. Notez qu'un `print` n'est pas un message à l'usager.
        3. Le service Web doit être disponible sur un serveur en ligne à partir d'un nom de domaine.
        4. Vous devez prévoir une requête GET pour lister les données de la base de données distante. Ceci n'a pas besoin d'être utilisé par l'application. Le but est de permettre, lors de la correction, de vérifier que les données soient bien synchronisées.
        5. Vous devez placer dans le dossier `dev` un fichier nommé `service-web.txt` dans lequel vous inscrirez l'URL qui donne accès à cette liste.
    2. **Autre service Web**, par exemple celui que vous avez développé dans le cadre du cours Services Web. Ce service doit être en lien avec le sujet de votre application. Le prof doit valider si ce service peut être utilisé ici.
        1. Il doit y avoir une fonctionnalité de votre application qui appelle le service Web.
        2. L'usager doit être informé si un problème survient lors de l'appel du service. En cas de réussite, si le résultat n'est pas visible à l'écran, un message doit aussi en informer l'usager. Notez qu'un `print` n'est pas un message à l'usager.
        3. Le service Web doit être disponible sur un serveur en ligne à partir d'un nom de domaine.
        4. Vous devez prévoir une requête GET pour démontrer au professeur que le service Web a bien réalisé la tâche pour laquelle il est conçu. Ceci n'a pas besoin d'être utilisé par l'application. Le but est de permettre, lors de la correction, de vérifier que le service a bien fait son travail.
        5. Vous devez placer dans le dossier `dev` un fichier nommé `service-web.txt` dans lequel vous inscrirez l'URL qui donne accès à cette information. Il faut également préciser le format des données attendues par le service Web de même que le format des données retournées.
    3. **Service Web préprogrammé**. Ce service doit être en lien avec le sujet de votre application. Le prof doit valider si ce service peut être utilisé ici.
        1. Il doit y avoir une fonctionnalité qui [appelle le service Web](../lecons/consommer-un-service-web-avec-swiftui.md).
        2. Si vous choisissez un service Web qui a déjà été utilisé en exercice (ex : OpenWeatherMap, Dog), vous devez aller plus loin que ce qui a été fait en exercice.
        3. L'usager doit être informé si un problème survient lors de l'appel du service. En cas de réussite, si le résultat n'est pas visible à l'écran, un message doit aussi en informer l'usager. Notez qu'un `print` n'est pas un message à l'usager.
        4. Vous devez placer dans le dossier `dev` un fichier nommé `service-web.txt` dans lequel vous inscrirez le format des données attendues par le service de même que le format des données retournées. Si le service Web ne peut pas être testé en GET, vous devez documenter la procédure pour tester le fonctionnement du service.
19. L'application doit faire une utilisation appropriée de la [vibration](../lecons/la-vibration.md).
20. Vous devez documenter les tests fonctionnels de l'application sur [Je Teste Tout!](https://jetestetout.apical.xyz/) et les faire co-corriger par un collègue de la classe. Le nombre de cas d'essai requis est spécifié dans la grille de correction. Dans Je Teste Tout, nommez votre application au format `MobileNomPrenom` et inscrivez-la au groupe `nvNejK44` (Applications mobiles 1 - H2026).
21. En plus du code de votre application, vous devez remettre une courte vidéo (durée maximale de 5 minutes) qui fait une démonstration complète de l'application et de ce qu'elle peut faire.
    1. La vidéo peut être enregistrée à l'aide de différentes techniques :  
        1. à partir du simulateur à l'aide de la fonction d'enregistrement vidéo intégrée au Mac  
        2. à partir du téléphone à l'aide de la fonction d'enregistrement d'écran intégrée au iPhone (faire glisser le coin supérieur droit et appuyer sur l'icône de cercles concentriques)  
        3. en filmant à l'aide d'un autre téléphone  
        4. avec une combinaison de ces techniques  
    2. La vidéo doit commencer par résumer ce que fait l'application et quel capteur elle utilise.  
    3. La vidéo doit faire une démonstration de l'application en français. Afin de démontrer la localisation, la vidéo doit ensuite montrer les écrans en anglais.  
    4. Une partie de la vidéo doit montrer l'utilisation du capteur et de la vibration. Tout ne peut donc pas être filmé à partir du simulateur. Astuce : pour faire entendre la vibration dans la vidéo, il est possible de placer le téléphone sur une cannette vide 😉 Notez que vous pouvez aussi simplement mentionner à quel moment la vibration a lieu.  
    5. La vidéo doit contenir une narration et il ne doit pas y avoir de bruit de fond dérangeant.  
    6. La vidéo doit faire la démonstration du bon fonctionnement du service Web et de la récupération des informations dans l'application.  
    7. La vidéo doit montrer l'écran de demande de permission si requis par le capteur.  
    8. Si la vidéo n'est pas remise avec le projet, les éléments qui ne peuvent pas être évalués avec le simulateur se verront attribuer la note 0.  
22. Le contenu du dossier `dev` est spécifié dans la grille de correction.  
