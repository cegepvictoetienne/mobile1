# Les tableaux

## Les tableaux Swift

Les tableaux en Swift ressemblent beaucoup aux tableaux en PHP.

Par contre, tous les éléments du tableau doivent avoir le même type.

```swift title="Swift"
let monTableau = ["valeur 1", "valeur 2", "valeur 3"]
```

Cette syntaxe permet d'initialiser un tableau plus facilement quand les éléments ont tous la même valeur au départ.

```swift title="Swift"
var monTableau = Array(repeating: "", count: 10)
```

Il est possible de déclarer un tableau vide à condition de spécifier son type.

```swift title="Swift"
var monTableau: [String] = []
```

Cette autre syntaxe est équivalente. On dira qu'elle utilise l'inférence de type (c'est-à-dire que le type n'est pas spécifié). Elle appelle le constructeur du type Array avec le type String : [String]()

```swift title="Swift"
var monTableau = [String]()
```

### Tableau d'instances d'une structure

Un tableau peut contenir n'importe quel type de données, incluant des instances d'une structure.

```swift title="Swift"
var items: [Item] = [
  Item(id: 1, code: "abc", titre: "Une table"),
  Item(id: 2, code: "def", titre: "Une chaise")
]
```

Il est également possible d'ajouter des éléments au tableau dans un deuxième temps.

```swift title="Swift"
var items: [Item] = []
items.append(Item(id: 1, code: "abc", titre: "Une table"))
```

### Tableau à deux dimensions

Voici la syntaxe pour déclarer un tableau à deux dimensions. Ici, c'est un tableau de Int et il est vide au départ.

```swift title="Swift"
var monTableau: [[Int]] = []
```

On aurait pu initialiser le tableau dès sa déclaration.

```swift title="Swift"
var monTableau: [[Int]] = [[0, 1, 2, 3, 4], [10, 11, 12, 13, 14]]
```

Pour donner la même valeur de départ à tous les éléments :

```swift title="Swift"
var monTableau: [[Int]] = Array(repeating: Array(repeating: 0, count: 5), count: 6)
```

Pour modifier une valeur de ce tableau :

```swift title="Swift"
monTableau[x][y] = 3
```

### Tableau avec données variées

Si jamais vous avez besoin d'un tableau qui contient différents types de données, la solution consiste à déclarer un protocole, de créer différentes structures qui répondent à ce protocole et d'utiliser ce protocole comme type de données dans le tableau.

??? info "Pour plus d'information"

    « Array ». Apple. <https://developer.apple.com/documentation/swift/array>

    « Collection Types ». Swift. <https://docs.swift.org/swift-book/LanguageGuide/CollectionTypes.html>

    « Constants, Variables and Types ». Dimitri Racordon. <https://kyouko-taiga.github.io/swift-thoughts/tutorial/chapter-1/>

## Quelques méthodes utiles pour manipuler des tableaux

Lorsque vous devez manipuler un tableau en Swift, vous avez à votre disposition de nombreuses méthodes, par exemple :

- [allSatisfy()](https://developer.apple.com/documentation/swift/array/allsatisfy(_:))
- [contains()](https://developer.apple.com/documentation/swift/array/contains(_:))
- [count()](https://developer.apple.com/documentation/swift/array/count)
- [dropFirst()](https://developer.apple.com/documentation/swift/array/dropfirst(_:))
- [first()](https://developer.apple.com/documentation/swift/array/first)
- [firstIndex()](https://developer.apple.com/documentation/swift/array/firstindex(of:))
- [insert()](https://developer.apple.com/documentation/swift/array/insert(_:at:))
- [map()](https://developer.apple.com/documentation/swift/array/map(_:)-9jnp5)
- [max()](https://developer.apple.com/documentation/swift/array/max())
- [min()](https://developer.apple.com/documentation/swift/array/min())
- [randomElement()](https://developer.apple.com/documentation/swift/array/randomelement())
- [reduce()](https://developer.apple.com/documentation/swift/array/reduce(_:_:))
- [remove()](https://developer.apple.com/documentation/swift/array/remove(at:)) (retirer un élément par sa position)
- [removeAll()](https://developer.apple.com/documentation/swift/array/removeall(where:)-5k61r) (retirer les éléments qui répondent à une condition)
- [replaceSubrange()](https://developer.apple.com/documentation/swift/array/replacesubrange(_:with:))
- [shuffle()](https://developer.apple.com/documentation/swift/array/shuffle())
- [sort()](https://developer.apple.com/documentation/swift/array/sort(by:))
- [sorted()](https://developer.apple.com/documentation/swift/array/sorted(by:)) (même chose que sort() mais retourne un tableau trié sans modifier l'original)
- [starts()](https://developer.apple.com/documentation/swift/array/starts(with:))

## Boucler dans un tableau

Je vous présente ici quelques techniques pour boucler dans les éléments d'un tableau.

### for

[La boucle for](https://docs.swift.org/swift-book/LanguageGuide/ControlFlow.html#ID121) permet de boucler facilement dans les éléments d'un tableau.

Cette syntaxe prend tout son sens si vous avez pris soin de donner un nom au pluriel au tableau, par exemple `valeurs`.

À l'intérieur de la boucle, l'élément qui est en cours de traitement portera ce nom mais au singulier, par exemple `valeur`.

```swift title="Swift"
for valeur in valeurs {
  print(valeur)
}
```

La fonction [zip()](https://developer.apple.com/documentation/swift/zip(_:_:)) permet de créer une séquence de paires dont les valeurs sont tirées de deux tableaux.

Autrement dit, elle associe le premier élément du premier tableau avec le premier élément du second tableau et ainsi de suite.

```swift title="Swift"
let films: [String] = ["Harry Potter", "Seigneur des anneaux", "Star Wars"]
let acteurs: [String] = ["Daniel Radcliffe", "Viggo Mortensen", "Mark Hamill"]

for(film, acteur) in zip(films, acteurs) {
  print("\(film): \(acteur)")
}
```

Voici un autre exemple qui permet de retrouver les indices d'un tableau.

```swift title="Swift"
let mots: [String] = ["Allô", "Bonjour", "Salut"]

for(i, mot) in zip(mots.indices, mots) {
  print("\(i): \(mot)")
}
```

La méthode [enumerated()](https://developer.apple.com/documentation/swift/array/enumerated()) permet elle aussi de travailler avec un tableau et ses indices.

```swift title="Swift"
let mots: [String] = ["Allô", "Bonjour", "Salut"]

for(i, mot) in mots.enumerated() {
  print("\(i): \(mot)")
}
```

### forEach()

Il est également possible d'utiliser la [méthode forEach()](https://developer.apple.com/documentation/swift/array/foreach(_:)).

```swift title="Swift"
let mots: [String] = ["Allô", "Bonjour", "Salut"]

mots.forEach{ mot in
  print(mot)
 }
```

Voici quelques exemples supplémentaires avec forEach().

```swift title="Swift"
let mots: [String] = ["Allô", "Bonjour", "Salut"]

mots.indices.forEach { i in
  print("\(i): \(mots[i])")
 }
```

Ici, on travaille avec la méthode enumerated().

```swift title="Swift"
let mots: [String] = ["Allô", "Bonjour", "Salut"]

mots.enumerated().forEach { (i, mot) in
  print("\(i): \(mot)")
 }
```

## Vérifier si le tableau contient une valeur donnée

La méthode [contains()](https://developer.apple.com/documentation/swift/array/contains(_:)) permet de vérifier si une valeur fait partie d'un tableau.

```swift title="Swift"
if valeurs.contains("abc") {
  ...
}
```

Dans le cas où on a un tableau d'objets, `contains()` permet également de vérifier si un des objets a une propriété avec la valeur recherchée.

```swift title="Swift"
var items: [Item] = [
  Item(id: 1, code: "abc", titre: "Une table"),
  Item(id: 2, code: "def", titre: "Une chaise")
]

if items.contains(where: { item in
  item.code == "abc"
 }) {
  ...
}
```

Cet extrait de code permet de retrouver l'élément qui correspond au critère de recherche.

```swift title="Swift"
let itemTrouve = items.first { item in
  item.code == "abc"
}
```

## allSatisfy()

La fonction [allSatisfy()](https://developer.apple.com/documentation/swift/array/allsatisfy(_:)) permet de vérifier rapidemement si tous les éléments d'un tableau répondent à une condition.

```swift title="Swift"
let resultats = [72, 58, 95, 86, 80]

if (resultats.allSatisfy { $0 >= 60 }) {
  print("Tous les élèves ont réussi l'examen!")
}
```

??? info "Pour plus d'information"

    « allSatisfy(_:) ». Apple. <https://developer.apple.com/documentation/swift/array/allsatisfy(_:)>

## Recherche dans un tableau ou dans un dictionnaire

### Tableau simple

La méthode [firstIndex(of:)](https://developer.apple.com/documentation/swift/array/2994720-firstindex) permet de retrouver la position d'un élément dans un tableau.

```swift title="Swift"
let monTableau = ["Premier élément", "Deuxième élément", "Troisième élément"]
...
let position = monTableau.firstIndex(of: "Deuxième élément")   // 1
```

### Tableau de structures

La méthode [firstIndex(where:)](https://developer.apple.com/documentation/swift/array/2994722-firstindex) permet d'effectuer une recherche plus diversifiée. Elle prend en paramètre une fonction anonyme qui permet de rechercher autre chose qu'une égalité.

Entre autres, elle permet de trouver la position d'un élément dans un tableau de structures.

```swift title="Swift"
struct Ami {
  var nomFamille: String
  var prenom: String
}
...

let amis: [Ami] = [
  Ami(nomFamille: "Lacasse", prenom: "Toto"),
  Ami(nomFamille: "Wilco", prenom: "Roger"),
  Ami(nomFamille: "Girard", prenom: "Andréanne")
]
...

if let position = amis.firstIndex(where: {
  $0.prenom == "Roger"
 }) {
  nomFamille = amis[position].nomFamille
 }
 else {
  nomFamille = "personne"
 }
```

### Dictionnaire

Pour rechercher la valeur qui correspond à une clé, il suffit d'accéder directement à cette valeur à partir de la clé.

Si la clé n'existe pas, on aura nil.

C'est pourquoi il faut prévoir ce qui se passera si jamais la clé n'existe pas. Ici, j'ai choisi d'imprimer le mot « aucun ».

```swift title="Swift"
let monDictionnaire:[String:String] = ["Nom":"Roger Wilco", "Spécialité":"SwiftUI", "Ville":"Victoriaville"]

 print(monDictionnaire["Nom"] ?? "aucun")   // Roger Wilco
 print(monDictionnaire["Téléphone"] ?? "aucun")   // aucun
```

Il aurait aussi été possible de gérer le cas où la clé n'existe pas comme suit :

```swift title="Swift"
let monDictionnaire:[String:String] = ["Nom":"Roger Wilco", "Spécialité":"SwiftUI", "Ville":"Victoriaville"]

if let valeur = monDictionnaire["Nom"] {
  print(valeur)
}
else {
  print("aucun")
}
```

Pour rechercher la clé qui correspond à une valeur dans un dictionnaire, il faut faire appel aux méthodes key() et value().

```swift title="Swift"
let monDictionnaire:[String:Int] = ["ABC":10, "DEF":3, "GHI":8]

 if let cle = monDictionnaire.first(where: { $0.value == 3 })?.key {
  print(cle)   // "DEF"
 }
```

??? info "Pour plus d'information"

    « How To Find an Item in an Array in Swift ». LearnAppMaking.com. <https://learnappmaking.com/find-item-in-array-swift/>

## Trier un tableau

La méthode [sort()](https://developer.apple.com/documentation/swift/array/sort()) permet de trier un tableau.

Le tableau original sera modifié.

```swift title="Swift"
var monTableau = ["mer", "plage", "ballon"]
monTableau.sort()   // monTableau contient désormais les valeurs ["ballon", "mer", "plage"]
```

Si vous désirez laisser le tableau original intact, il faut plutôt utiliser [sorted()](https://developer.apple.com/documentation/swift/array/sorted()).

```swift title="Swift"
var monTableau = ["mer", "plage", "ballon"]
var tableauTrie = monTableau.sorted()   // tableauTrie contient désormais les valeurs ["ballon", "mer", "plage"]
```

Une [autre variante de cette méthode](https://developer.apple.com/documentation/swift/array/sorted(by:)) permet de spécifier comment les éléments seront triés.

```swift title="Swift"
var monTableau = ["mer", "plage", "ballon"]
var tableauTrie = monTableau.sorted(by: >)   // tableauTrie contient désormais les valeurs ["plage", "mer", "ballon"]
```

### Tableau d'instances

Si vous désirez trier un tableau d'instances selon une des propriétés, voici la recette.

```swift title="Swift"
var items: [Item] = [
  Item(id: 1, code: "abc", titre: "Une table"),
  Item(id: 2, code: "ghi", titre: "Un ordinateur")
  Item(id: 3, code: "def", titre: "Une chaise")
]

var itemsTries = items.sorted(by: { instance1, instance2 in
  instance1.code < instance2.code
 })
```

??? info "Pour plus d'information"

    « How to Sort an Array in Swift ». Cocoacasts. <https://cocoacasts.com/swift-fundamentals-how-to-sort-an-array-in-swift>
