# Aller plus loin avec SwiftData

## Modifier le tri ou le filtre d'une requête après que la requête ait été exécutée

Quand on retrouve des données de la base de données à l'aide de @Query, il faut préciser le tri et le filtre désirés dès la déclaration de la propriété.

```swift title="SwiftUI"
@Query(filter: #Predicate<Item> { $0.categorie.code == 'ABC' }, sort: \Item.code) var items: [Item]
```

Mais comment faire si on désire permettre à l'usager de modifier le tri ou de modifier les conditions du filtre?

Il faut utiliser une petite astuce. Elle consiste à créer une sous-vue dans laquelle un constructeur reçoit les informations sur le tri ou le filtre souhaité.

Une ou plusieurs variables d'état dans la vue principale permettront de spécifier le tri ou le filtre.

La vue principale appellera la sous-vue avec les paramètres désirés puis le constructeur de la sous-vue ajustera la requête.

```swift title="Fichier ContentView.swift"
struct ContentView: View {

 @State private var optionTriChoisie: Int = 1
 @State private var optionFiltreChoisie: Int = 1

 let optionsTri: [Option] = [
  Option(id: 1, texte: "Ordre ascendant"),
  Option(id: 2, texte: "Ordre descendant")
 ]
let optionsFiltre: [Option] = [
  Option(id: 1, texte: "Afficher les inactifs"),
  Option(id: 2, texte: "Masquer les inactifs")
 ]
var body: some View {
  NavigationStack {
    ListeItems(optionTriChoisie: optionTriChoisie, optionFiltreChoisie: optionFiltreChoisie)
      .navigationTitle("Test requêtes dynamiques")
      .toolbar {
        ToolbarItem(placement: .topBarLeading, content: {
          Menu {
            Picker("", selection: $optionTriChoisie) {
              ForEach(optionsTri) { option in
                Text(option.texte)
              }
            }
          } label: {
            Text("Tri")
          }
        })
        ToolbarItem(placement: .topBarTrailing, content: {
          Menu {
            Picker("", selection: $optionFiltreChoisie) {
              ForEach(optionsFiltre) { option in
                Text(option.texte)
              }
            }
          } label: {
            Text("Filtre")
          }
        })
      }
    }
  }
}
```

Important : dans la sous-vue, il doit y avoir une barre de soulignement devant le nom de la propriété qui reçoit les données de la base de données. En effet, on travaille ici avec une propriété encapsulée, aussi appelée **propriété privée sous-jacente** (en anglais : **backing property**) qui a été créée automatiquement lors du @Query.

Autrement dit, ce n'est pas la propriété qui est changée mais bien la requête qui initialise la propriété, disponible via la propriété encapsulée.

```swift title="Fichier ListeItems.swift"
struct ListeItems: View {
  @Query(filter: #Predicate<Item> { $0.actif == true },sort: \Item.nom) var items: [Item]

  init(optionTriChoisie: Int, optionFiltreChoisie: Int) {
    var tri: [SortDescriptor<Item>]
    var predicate = #Predicate<Item> {
      $0.actif == true
    }
    var filtrer: Bool = false

    if optionTriChoisie == 1 {
      print("Ordre ascendant")
      tri = [SortDescriptor(\Item.nom)]
    }
    else {
      print("Ordre descendant")
      tri = [SortDescriptor(\Item.nom, order: .reverse)]
    }

    if optionFiltreChoisie == 1 {
      print("Afficher inactifs")
    }
    else {
      print("Masquer inactifs")
      filtrer = true
    }

    if filtrer {
      _items = Query(filter: predicate, sort: tri)
    }
    else {
      _items = Query(sort: tri)
    }
  }

  var body: some View {
    List (items) { item in
      HStack(spacing: 4) {
        Text(item.nom)
          .foregroundColor(item.actif ? Color.black : Color.gray)
        Spacer()
        Button(
          action: {
            item.actif.toggle()
        }) {
          Image(systemName: item.actif ? "antenna.radiowaves.left.and.right.slash" : "antenna.radiowaves.left.and.right")
        }
      }
    }
  }
}
```

??? info "Pour plus d'information"

    « How to dynamically change a query's sort order or predicate ». Hacking with Swift. <https://www.hackingwithswift.com/quick-start/swiftdata/how-to-dynamically-change-a-querys-sort-order-or-predicate>

    «  Dynamically filtering our SwiftData query  ». Hacking with Swift. <https://www.hackingwithswift.com/books/ios-swiftui/dynamically-filtering-our-swiftdata-query>

## Retrouver l'identifiant d'un enregistrement avec SwiftData

Dans la majorité du code SwiftData que vous écrirez, vous n'aurez pas besoin de connaître l'identifiant d'un enregistrement.

C'est SwiftData qui se charge de gérer cet identifiant et de l'utiliser lorsque requis dans les clés étrangères.

Pourtant, dans certaines situations, il sera requis de travailler avec l'identifiant d'un enregistrement. L'identifiant peut à ce moment être retrouvé à l'aide de [persistentModelID](https://developer.apple.com/documentation/swiftdata/persistentmodel/persistentmodelid).

```swift title="SwiftUI"
List (categorie.items!.sorted(by: {$0.code < $1.code})) { item in
  ...
  Button(
    role: .destructive,
    action: {
      // ici, on recherche dans un tableau d'items l'élément qui correspond à l'item sur leqel on vient de cliquer
      if let index = categorie.items!.firstIndex(where: {$0.persistentModelID == item.persistentModelID}) {
        categorie.items!.remove(at: index)
      }
  }) {
    Image(systemName: "trash")
      .padding(.leading)
  }
}
```

Lorsqu'un objet provient de la base de données, la valeur de persistentModelID est fiable.

Par contre, lorsqu'un nouvel objet est instancié sans effectuer une requête à la base de données, le persistentModelID est temporaire et ne deviendra fiable que lorsque l'objet sera enregistré.

## Retrouver un seul enregistrement avec SwiftData

Lorsqu'on effectue une [requête avec @Query](swiftdata.md#requetes-pour-retrouver-les-donnees-de-la-base-de-donnees-query) dans une application SwiftUI qui utilise SwiftData, les données recueillies sont toujours placées dans un tableau d'objets et ce, même si la requête ne retrouve qu'un seul enregistrement.

```swift title="SwiftUI"
import SwiftUI
import SwiftData

struct ContentView: View {
  @Query(filter: #Predicate<Item> { $0.code == "abc) }) var items: [Item]

  var body: some View {
    ...
  }
}
```

Normalement, ce comportement devrait convenir à votre application. Les traitements qui nécessitent un enregistrement particulier seront effectués [dans une vue enfant qui reçoit cet enregistrement en paramètre](transferer-des-informations-entre-les-vues.md#de-la-vue-enfant-vers-la-vue-parent-binding-et-bindable).

Dans les cas d'exception où vous avez besoin de travailler avec un objet qui n'est pas dans un tableau sans passer par une vue parent, vous pouvez procéder comme ceci :

```swift title="SwiftUI"
@Query(filter: #Predicate<Item> { $0.code == "abc) }) var items: [Item]
var itemTempo: Item? { item.first }   // pas possible d'avoir une variable d'état ici, sinon erreur Property wrapper cannot be applied to a computed property
@State private var item: Item?

var body: some View {
  VStack {
    ...
  }
  .onAppear(perform: {
    item = itemTempo
  })
}
```

## Renommer un champ après que la base de données ait été générée par SwiftData

Si vous désirez renommer une propriété du modèle après que SwiftData ait créé la table correspondante, vous devez prendre une précaution.

Le fait de renommer une propriété fera en sorte que SwiftData créera un nouveau champ dans la base de données.

Si vous désirez que SwiftData renomme le champ, il faut ajouter la macro [@Attribute](https://developer.apple.com/documentation/swiftdata/attribute(_:originalname:hashmodifier:)) pour lier le nouveau nom à l'ancien.

```swift title="SwiftUI"
@Model
final class Item {
  ...
  @Attribute(originalName: "anciennom") var nouveaunom: String
}
```

## Ajouter un champ au modèle qui ne doit pas être enregistré dans la base de données par SwiftData

Par défaut, pour chacune des propriétés déclarées dans le modèle, SwiftData générera un champ dans la base de données.

Il est possible de modifier ce comportement pour qu'une propriété ne soit utilisée qu'en mémoire vive. Le code pourra travailler avec cette propriété sans qu'elle soit automatiquement enregistrées dans un champ.

```swift title="SwiftUI"
@Model
final class Item {
  ...
  @Transient
  var champMemoireVive: String = ""
}
```

Notez que si la classe comprend des propriétés calculées, ces propriétés ne seront pas non plus enregistrées dans la base de données.

```swift title="SwiftUI"
@Model
final class Eleve {
  var prenom: String
  var nomFamille: String

  // propriété calculée - pas enregistrée dans la BD
  var nomComplet: String {
    self.prenom + " " + self.nomFamille
  }
}
```

## Gérer les versions de la base de données SwiftData

Quand vous apportez des modifications à la structure de la base de données, SwiftData est capable de gérer automatiquement les versions de la base de données afin d'effectuer les migrations sur les appareils où l'application est installée.

If faut cependant que chaque version soit correctement identifiée à l'aide du protocole [VersionedSchema](https://developer.apple.com/documentation/swiftdata/versionedschema).

Avant d'effectuer la modification au modèle, placez le modèle original dans un `VersionedSchema`. Le nouveau modèle sera dans le `VersionedSchema` suivant.

Vous pouvez nommer les versions comme bon vous semble. Ici, j'ai simplement utilisé V1, V2, etc.

```swift title="SwiftUI"
enum MonProjetSchemaV1: VersionedSchema {
  @Model
  final class Item {
    ...
    var anciennom: String
  }

  @Model
  final class Cagegorie {
    ...
  }
}

enum MonProjetSchemaV2: VersionedSchema {
  @Model
  final class Item {
    ...
    @Attribute(originalName: "anciennom") var nouveaunom: String
  }

  @Model
  final class Cagegorie {
    ...
  }
}
```

Il faut ensuite établir le plan de migration à l'aide du protocole [SchemaMigrationPlan](https://developer.apple.com/documentation/swiftdata/schemamigrationplan).

Dans le cas de modifications mineures, par exemple la modification du nom d'un champ, SwiftData pourra effecteur la migration sans code supplémentaire. Il suffit de lui mentionner le nom du schéma original et le nom du schéma ciblé.

```swift title="SwiftUI"
enum MonProjetMigrationPlan: SchemaMigrationPlan {
  static var schemas: [any VersionedSchema.Type] {
    [MonProjetSchemaV1.self, MonProjetSchemaV2.self]
  }

  static var stages: [MigratonStage] {
    [migrateV1toV2]
  }

  static let migrateV1toV2 = MigrationStage.custom(
    fromVersion: MonProjetSchemaV1.self,
    toVersion: MonProjetSchemaV2.self
  )
}
```

Si les modifications nécessitaient du code, par exemple modifier les données en place, il serait possible de fournir ce code dasn la closure willMigrate. SwiftData effectuera ce code avant de procéder à la migration.

```swift title="SwiftUI"
enum MonProjetMigrationPlan: SchemaMigrationPlan {
  static var schemas: [any VersionedSchema.Type] {
    [MonProjetSchemaV1.self, MonProjetSchemaV2.self]
  }

  static var stages: [MigratonStage] {
    [migrateV1toV2]
  }

  static let migrateV1toV2 = MigrationStage.custom(
    fromVersion: MonProjetSchemaV1.self,
    toVersion: MonProjetSchemaV2.self,
    willMigrate: { context in
      // écrire ici le code à réaliser avant de procéder à la migration
    }, ditMigrate: nil
  )
}
```

Pour que SwiftData puisse procéder à la migration, il faut lui spécifier le plan de migration.

Ceci sera réalisé dans le fichier principal de l'application.

```swift title="SwiftUI"
import SwiftUI
import SwiftData

@main
struct MonProjetApp: App {
  let container = ModelContainer(
    for: Item.self,
    migrationPlan: MonProjetMigrationPlan.self
  )

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
    .modelContainer(for: Item.self)
  }
}
```

??? info "Pour plus d'information"

    « Model your schema with SwiftData ». Apple. <https://developer.apple.com/videos/play/wwdc2023/10195/>

    « How to create a complex migration using VersionedSchema ». Hacking with Swift. <https://www.hackingwithswift.com/quick-start/swiftdata/how-to-create-a-complex-migration-using-versionedschema>
