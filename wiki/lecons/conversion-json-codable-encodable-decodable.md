# Conversion JSON (Codable, Encodable, Decodable)

## Codable : pour permettre l'encodage et le décodage JSON

Quand une structure ou une classe répond au protocole `Encodable`, il est possible d'encoder ses instances, par exemple au format JSON.

Avec le protocole `Decodable`, il sera possible de les décoder.

Le type [Codable](https://developer.apple.com/documentation/swift/codable) est un alias pour les protocoles `Encodable` et `Decodable`. Il permet donc d'effectuer l'encodage et le décodage.

L'encodage est parfois appelé [sérialisation](https://fr.wikipedia.org/wiki/S%C3%A9rialisation) et le décodage, désérialisation.

Ceci permettra notamment [de transférer des données à un service Web et de recevoir la réponse de ce service Web](fonctions-obsoletes-ou-anciennes-syntaxes.md#consommer-un-service-web-technique-traditionnelle).

Prenons un modèle `Item` défini comme suit :

```swift title="Swift"
struct Item: Codable {
  var code: String
  var titre: String
}
```

### Encoder en JSON

Dans cet exemple, on a un tableau de ce modèle, par exemple :

```swift title="Swift"
let items = [
  Item(code:"000A1", titre:"Item 1"),
  Item(code:"000A2", titre:"Item 2")
]
```

Pour obtenir une version JSON de ce tableau, on travaillera avec [JSONEncoder().encode()](https://developer.apple.com/documentation/foundation/jsonencoder/2895034-encode).

Il faut prévoir ce qui se passera si jamais les données ne pouvaient pas être encodées.

L'instruction [guard](le-langage-swift-reference.md#linstruction-guard) permet de sortir du bloc de code en cours, par exemple de la fonction, si une condition n'est pas respectée. Le code pourrait également être réalisé à l'aide d'un `if` mais `guard` assure que le bloc de code sera terminé si la condition est évaluée à false.

```swift title="Swift"
guard let itemsJSON = try? JSONEncoder().encode(items) else {
  print("Impossible d'encoder les items en JSON")
  return
 }
...
```

Remarquez le point d'interrogation qui suit le `try`. Il permet de gérer le cas où l'encodage échouerait. Grâce au point d'interrogation, un problème d'encodage initialisera la variable itemsJSON à `nil` au lieu de propager l'erreur.

Si l'information encodée en JSON est passée à un service Web écrit en PHP, il recevra les données sous cette forme :

```text title="Données reçues"
Array
(
    [0] => stdClass Object
        (
            [code] => 000A1
            [titre] => Item 1
        )

    [1] => stdClass Object
        (
            [code] => 000A2
            [titre] => Item 2
        )
)
```

### Décoder du JSON

À l'inverse, quand on a une représentation JSON qu'on désire manipuler, il faut effectuer un décodage.

On obtiendra une variable dont le type dépend de la structure des données JSON. Ce pourrait être une instance d'une classe ou d'une structure si les données JSON correspondent aux propriétés de cette classe ou structure. Ce pourrait aussi être un tableau d'instances.

En fait, Swift tentera d'initialiser une variable selon le type qu'on lui fournit comme premier paramètre dans la méthode [JSONDecoder().decode()](https://developer.apple.com/documentation/foundation/jsondecoder/2895189-decode). Pour fournir le type, il faut faire suivre le type par le mot-clé `self`. Ce type doit répondre minimalement au protocole Decodable.

Évidemment, il faudra prévoir ce qui se passe si jamais le décodage ne fonctionne pas.

Dans cet exemple, les données décodées seront récupérées dans un tableau d'Items puisque c'est ce à quoi les données encodées en JSON correspondent.

J'ai utilisé un `if` plutôt qu'un `guard` afin d'illustrer les deux techniques. Ceci implique qu'il faut réagir correctement dans le code en cas d'échec puisque la fonction ne se terminera pas immédiatement.

```swift title="Swift"
if let itemsDecodes = try? JSONDecoder().decode([Item].self, from: itemsJSON) {
  ...
 }
else {
  print("Impossible de décoder les items")
  print("Chaîne JSON: \(String(describing: String(data:itemsJSON, encoding: .utf8)))")
  ...
}
```

Dans l'application Swift, les données décodées prendront cette forme :

```text title="Données décodées"
[
    MonProjet.Item(
        code: "000A1", titre: "Item 1"
    ),

    MonProjet.Item(
        code: "000A2", titre: "Item 2"
    )
]
```

??? info "Pour plus d'information"

    « Encoding and Decoding Custom Types ». Apple. <https://developer.apple.com/documentation/foundation/archives_and_serialization/encoding_and_decoding_custom_types>

    « Complete Guide to Codable — Decodable ». Medium - Flawless iOS. <https://medium.com/flawless-app-stories/complete-guide-to-codable-decodable-b1ff696da24f>

    «  SOLVED: Decoding JSON data - Error response  ». Hacking with Swift. <https://www.hackingwithswift.com/forums/swiftui/decoding-json-data/3024>

    « Ultimate Guide to JSON Parsing with Swift ». Ben Scheirman. <https://benscheirman.com/2017/06/swift-json.html>

    « JSON Decoding in Swift with Codable: A Practical Guide ». Matteo Manferdini. <https://matteomanferdini.com/codable/>

## Rendre un modèle SwiftData encodable ou décodable

Lorsque les données à encoder proviennent d'un modèle SwiftData, il faut prendre une précaution pour assurer que le modèle réponde au protocole `Encodable` ou à `Decodable` ou encore aux deux (`Codable`).

Sans cette précaution, vous obtiendrez les messages d'erreur « Type 'Item' does not conform to protocol 'Encodable' » ou « Type 'Item' does not conform to protocol 'Decodable' ».

Ceci est dû au fait que la macro `@Model` ajoute du code pour nous et c'est une partie de ce code qui ne répond pas à ces protocoles.

Pour régler ce problème, il faut spécifier comment encoder ou décoder les données de ce modèle.

Ceci est réalisé à l'aide de ces étapes :

- Définir une [énumération](le-langage-swift-reference.md#les-enumerations) nommée `CodingKey` qui répond au protocole [CodingKey](https://developer.apple.com/documentation/swift/codingkey) pour lister toutes les propriétés qui doivent pouvoir être encodées ou décodées. Le nom de chaque cas de l'énumération doit correspondre au nom d'une propriété à encoder ou à décoder.

  ```swift title="SwiftUI"
  @Model
  final class Item: Codable {   // ou Encodable, ou Decodable
    var code: String
    var titre: String

    enum CodingKeys: CodingKey {
      case code, titre
    }
    ...
  }
  ```
- Pour que la classe réponde au protocole `Encodable`, ajouter une méthode `encode(to:)` pour déterminer comment les valeurs peuvent être encodées.

  ```swift title="SwiftUI"
  @Model
  final class Item: Encodable {   // ou Codable
    ...
    func encode(to encoder: Encoder) throws {
      var container = encoder.container(keyedBy: CodingKeys.self)
      try container.encode(code, forKey: .code)
      try container.encode(titre, forKey: .titre)
    }
  }
  ```
- Pour que la classe réponde au protocole `Decodable`, ajouter un constructeur `init(from:)` pour déterminer comment les valeurs peuvent être décodées. Assurez-vous d'utiliser le bon type pour le décodage (dans l'exemple : `String.self`).

  ```swift title="SwiftUI"
  @Model
  final class Item: Decodable {   // ou Codable
    ...
    required init(from decoder: Decoder) throws {
      let container = try decoder.container(keyedBy: CodingKeys.self)
      self.code = try container.decode(String.self, forKey: .code)
      self.titre = try container.decode(String.self, forKey: .titre)
    }
  }
  ```

Il est maintenant possible d'encoder en JSON des objets de la classe Item ou de décoder du JSON pour instancier des objets de cette classe.

??? info "Pour plus d'information"

    « How to make SwiftData models conform to Codable ». Hacking with Swift. <https://www.hackingwithswift.com/quick-start/swiftdata/how-to-make-swiftdata-models-conform-to-codable>

    « Making your SwiftData models Codable ». Donny Wals. <https://www.donnywals.com/making-your-swiftdata-models-codable/>

## Encodage et décodage avec des tables liées

On a vu qu'il était possible d'indiquer précisément comment [encoder](conversion-json-codable-encodable-decodable.md#rendre-un-modele-swiftdata-encodable-ou-decodable) les instances d'un modèle SwiftData.

Lorsque le modèle SwiftData contient des références à d'autres modèles, par exemple pour définir une relation entre des tables, il faut s'assurer que chaque modèle réponde lui aussi au protocole Codable.

Attention : dans la classe enfant (celle qui contient la clé étrangère vers la table parent), il ne faut pas encoder la clé étrangère. En effet, puisque la classe parent encode déjà le tableau d'objets de la classe enfant, ceci créerait une boucle sans fin.

```swift title="Classe parent (SwiftUI)"
@Model
final class Categorie : Encodable {
  var titre: String
  var items: [Item] = []   // Item devra également répondre au protocole Encodable

  enum CodingKeys: CodingKey {
    case titre, items
  }
  ...

  func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    try container.encode(titre, forKey: .titre)
    try container.encode(items, forKey: .items)
  }
}
```

```swift title="Classe enfant (SwiftUI)"
@Model
final class Item: Encodable {
  var code: String
  var titre: String
  var categorie: Categorie?

  enum CodingKeys: CodingKey {
    case code, titre, categorie
  }
  ...

  func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    try container.encode(code, forKey: .code)
    try container.encode(titre, forKey: .titre)
    try container.encode(categorie, forKey: .categorie)   // il ne faut pas encoder la clé étrangère
  }
}
```

## Encoder correctement une date

La gestion des dates est toujours particulière dans les différents langages de programmation.

Et le langage Swift ne fait pas exception.

Je vous explique ici comment encoder correctement les dates à l'aide du protocole [Encodable](conversion-json-codable-encodable-decodable.md#codable-pour-permettre-lencodage-et-le-decodage-json).

### Comment la date est représentée dans Swift

Par défaut, Swift encode les dates en tant qu'un nombre de type `Double` qui représente les secondes écoulées [entre la date représentée et le 1er janvier 2001](https://developer.apple.com/documentation/foundation/nsdate/1409769-init).

Par exemple, si une date représente le `8 mai 2024 à 13:52:35` dans le fuseau horaire de Montréal, sa version encodée donnera le nombre `736883555.662463`.

Si vous êtes curieux de savoir comment retrouver ce nombre, entrez cette commande dans une [fenêtre lldb](deboguer-une-application-swiftui.md#fenetre-de-debogage-de-bas-niveau-lldb-low-level-debugger) en remplaçant `laDate` par le nom de la variable de type `Date` que vous désirez explorer.

```text title="Fenêtre lldb"
po laDate
```

```text title="Résultat à l'écran"
(lldb) po laDate
▿ 2024-05-08 17:52:35 +0000
  - timeIntervalSinceReferenceDate : 736883555.662463
```

Remarquez que la date en format lisible est donnée ici pour le fuseau horaire GMT (Greenwich Mean Time), indiqué par le `+0000`.

### Comment transformer la date lors de l'encodage

Si vous devez envoyer une date à un API, il est souvent plus prudent de la convertir en chaîne avant de l'envoyer. En effet, certains langages représentent les dates en tant que nombre de secondes écoulées entre la date et le 1er janvier 1970 plutôt que 2001. Problème en vue...

Lorsque la date à convertir fait partie d'un modèle SwiftData, la conversion pourra être réalisée comme suit :

```swift title="SwiftUI"
@Model
final class MonModele: Encodable {
  var echeance: Date
  ...

  enum CodingKeys: CodingKey {
    case echeance, ...
  }

  func encode(to encoder: Encoder) throws {
    // pour encoder les dates
    let dateFormatter = DateFormatter()
    dateFormatter.dateFormat = "yyyy-MM-dd HH:mm:ss"

    var container = encoder.container(keyedBy: CodingKeys.self)
    try container.encode(dateFormatter.string(from: dateAjout), forKey: .dateAjout)
    ...
  }
}
```

Avec ce code, chaque date sera automatiquement encodée au format spécifié.

Par exemple, la date `736883555.662463`, une fois encodée, deviendra "`2024-05-08 13:52:35`".

Remarquez que dans cet exemple, puisque le `DateFormatter` n'a pas de configuration `timeZone`, la chaîne tient compte du fuseau horaire configuré sur l'appareil (ici : Montréal).

### Gérer le fuseau horaire

La représentation interne de la date est toujours pour le fuseau horaire GMT. Par contre, la version encodée peut représenter la date du fuseau horaire de votre choix.

Il suffit de configurer l'attribut [timeZone](https://developer.apple.com/documentation/foundation/dateformatter/1411406-timezone) du `DateFormatter`.

Sans cette configuration, la date sera toujours donnée pour le fuseau horaire configuré sur l'appareil.

Par exemple, si vous désirez utiliser le fuseau horaire GMT :

```swift title="SwiftUI"
// pour encoder les dates
let dateFormatter = DateFormatter()
dateFormatter.dateFormat = "yyyy-MM-dd HH:mm:ss"
dateFormatter.timeZone = TimeZone(abbreviation: "GMT")
```

Il est également possible de forcer l'utilisation d'un fuseau horaire précis, par exemple le fuseau horaire de Montréal et ce, peu importe comment le téléphone est configuré :

```swift title="SwiftUI"
// pour encoder les dates
let dateFormatter = DateFormatter()
dateFormatter.dateFormat = "yyyy-MM-dd HH:mm:ss"
dateFormatter.timeZone = TimeZone(identifier: "America/Toronto")
```

## Vérifier le contenu d'une chaîne JSON

Dans une application SwiftUI, lorsqu'on [encode des données au format JSON](conversion-json-codable-encodable-decodable.md#codable-pour-permettre-lencodage-et-le-decodage-json), le débogage sera facilité si on connaît la technique pour vérifier le résultat de l'encodage.

Par défaut, quand on fait un [print()](deboguer-une-application-swiftui.md#print-debugprint-dump) de la chaîne encodée, on ne voit que sa taille.

```swift title="Fichier Models/Item.swift"
struct Item: Encodable {
  var code: String
  var titre: String
}
```

```swift title="Swift"
func encoder(item: Item) {
  guard let itemJSON = try? JSONEncoder().encode(item) else {
    print("Impossible d'encoder l'item en JSON")
    return
  }

  print(itemJSON)   // affiche 33 bytes - pas très intéressant :-(
}
```

Il faut savoir que la valeur convertie en JSON est de type [Data](https://developer.apple.com/documentation/foundation/data).

Pour voir la chaîne qui se cache dans cette variable, il faut [instancier un String()](https://developer.apple.com/documentation/swift/string/init(decoding:as:)).

```swift title="Swift"
print(String(data: itemJSON, encoding: .utf8) ?? "Impossible d'instancier la chaîne en UTF-8.")
```

```text title="Sortie Standard"
{"titre":"Item ABC","code":"abc"}
```

Pour avoir un affichage plus facile à lire, surtout quand la chaîne JSON est complexe, on peut spécifier le format [.prettyPrinted](https://developer.apple.com/documentation/foundation/jsonserialization/writingoptions/prettyprinted) lors de l'encodage.

```swift title="Swift"
let encoder = JSONEncoder()
 encoder.outputFormatting = .prettyPrinted

guard let itemJSON = try? encoder.encode(item) else {
  print("Impossible d'encoder l'item en JSON")
  return
}

print(String(data: itemJSON, encoding: .utf8) ?? "Impossible d'instancier la chaîne en UTF-8.")
```

 Dans la sortie Standard de Xcode, on verra ceci :

```text title="Sortie Standard"
{
  "code" : "abc",
  "titre" : "Item ABC"
}
```
