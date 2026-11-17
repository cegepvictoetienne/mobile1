# La persistance des données

## Qu'est-ce que la persistance des données?

La persistance des données, c'est le concept selon lequel les données continuent à exister même après qu'on ait éteint l'application ou l'ordinateur sur lequel elle tourne.

En clair, la persistance des données correspond à l'enregistrement des données sur disque, que ce soit dans un fichier plat ou dans une base de données plus sophistiquée.

Sur une application mobile, il y a un autre concept dont il faut tenir compte : les données locales vs les données distantes.

Il est important de permettre l'enregistrement des données même en l'absence de réseau. Cependant, on voudra généralement synchroniser les données locales avec des données infonuagiques afin de rendre l'information disponible sur plusieurs appareils.

Cette synchronisation permettra également d'assurer que les informations soient automatiquement disponibles si on brise/perd/change notre téléphone.

### Pour plus d'information

« Persistance (informatique) ». Wikipédia. <https://fr.wikipedia.org/wiki/Persistance_(informatique)>

« Faites persister vos données dans votre application iOS ». OpenClassrooms. <https://openclassrooms.com/fr/courses/4871481-faites-persister-vos-donnees-dans-votre-application-ios/5417778-decouvrez-la-persistance-des-donnees>

## Option pour enregistrer les données sous iOS

Il existe plusieurs façon pour faire persister les données sur iOS.

En voici quelques-unes :

- [UserDefaults](preferences-utilisateur-avec-userdefaults.md), qui peut être interfacé facilement avec l'attribut [@AppStorage](les-preferences-utilisateur.md#appstorage), pour le stockage de quelques paires clé-valeur
- [CoreData](https://developer.apple.com/documentation/coredata), un ORM (**Object Relational Mapper**), c'est-à-dire une couche d'abstraction entre l'application et la base de données. CoreData peut stocker les données de différentes façons, par exemple avec SQLite (en utilisant une structure précise), XML, Binary Store.
- [SwiftData](https://developer.apple.com/documentation/swiftdata), qui a été introduit avec iOS 17 en 2023. Il s'agit d'un ORM basé sur CoreData mais plus simple et efficace. Par contre, il offre moins de fonctionnalités que CoreData.
- SQLite, qui peut être utilisé seul ou encore à l'aide d'une bibliothèque pour faciliter son utilisation, par exemple [GRDB.swift](https://github.com/groue/GRDB.swift), [SQLite.swift](https://github.com/stephencelis/SQLite.swift), [SQLiteDB](https://github.com/FahimF/SQLiteDB)
- [Realm](https://realm.io/)
- [Couchbase](https://developer.couchbase.com/mobile/)
- [Firebase](https://firebase.google.com/docs/ios/setup)
- etc.

### Pour plus d'information

« What Is the Difference Between Core Data and SQLite ». Cocoacasts. <https://cocoacasts.com/what-is-the-difference-between-core-data-and-sqlite>
