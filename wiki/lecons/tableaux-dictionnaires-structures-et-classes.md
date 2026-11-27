# Tableaux, dictionnaires, structures et classes

## Les tableaux Swift

Les tableaux en Swift doivent avoir le même type.

```swift title="Swift"
let monTableau = ["valeur 1", "valeur 2", "valeur 3"]
```

Cette syntaxe permet d'initialiser un tableau plus facilement quand les éléments ont tous la même valeur au départ.

```swift title="Swift"
var monTableau = Array(repeating: "", count: 10)
```

Il est possible de déclarer un tableau vide à condition de spécifier son type.

```swift title="Swift"
// Comme ceci : (explicite)
var monTableau: [String] = []
// ou comme cela : (par inférence)
var monTableau2 = [String]()
```

### Tableau d'instances d'une structure

Un tableau peut contenir n'importe quel type de données, incluant des instances d'une structure.

```swift title="Swift"
var items: [Item] = [
  Item(id: 1, code: "abc", titre: "Une table"),
  Item(id: 2, code: "def", titre: "Une chaise")
]
```

Pour ajouter des éléments au tableau :  

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

## Boucler dans un tableau

Voici quelques techniques pour boucler dans les éléments d'un tableau.

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

## Les dictionnaires

Un dictionnaire, parfois appelé **tableau associatif**, est un type de tableau dont les données sont regroupées en paires clé-valeur.

Toutes les clés doivent être du même type et toutes les valeurs doivent être du même type, qui peut être différent du type des clés.

### Déclaration et initialisation

Pour déclarer un dictionnaire vide :

```swift title="Swift"
var monDictionnaire = [String:Int]()
// ou
var monDictionnaire2:[String:Int] = [:]
```

On peut également le remplir dès sa déclaration :

```swift title="Swift"
var monDictionnaire:[String:Int] = ["ABC":10, "DEF":3, "GHI":8]
```

Pour ajouter une valeur, il suffit d'utiliser une clé qui n'existe pas encore.

```swift title="Swift"
monDictionnaire["JKL"] = 25
```

### Accéder à un élément

Plutôt que de retrouver une information à l'aide d'un indice numérique, on retrouvera la valeur d'un tableau associatif à partir de sa clé.

```swift title="Swift"
let valeur = monDictionnaire["DEF"]   // 3
```

### Boucler dans le dictionnaire

Pour boucler dans les éléments du dictionnaire, la boucle for est toute indiquée.

```swift title="Swift"
for (cle, valeur) in monDictionnaire {
  print("Clé: \(cle) Valeur: \(valeur)")
}
```

On peut également utiliser la propriété [keys()](https://developer.apple.com/documentation/swift/dictionary/keys-swift.struct). Ceci retourne une collection. On convertira le résultat en tableau à l'aide de [Array()](https://developer.apple.com/documentation/swift/array/init(_:)-236cl).

```swift title="Swift"
let cles = Array(monDictionnaire.keys)
var valeur: Int

for cle in cles {
  valeur = monDictionnaire[cle]!
  print(cle)
  print(valeur)
 }
```

Remarquez le point d'exclamation dans l'instruction qui retrouve la valeur. Dans ce contexte, on l'appelle [**implicitly unwrapped optional**](https://swiftsenpai.com/swift/making-sense-of-swift-operators/).

Si on ne le met pas, on obtiendra cet avertissement : « Expression implicitly coerced from 'Int?' to 'Any' ».

C'est que le compilateur nous informe que `monDictionnaire[cle]` pourrait être nul. Il demande ce qu'il doit faire si ça arrive afin de ne pas faire planter le programme.

Avec le point d'exclamation – qu'il faut utiliser seulement dans des situations très spécifiques – on informe le compilateur que c'est certain que la valeur ne peut pas être nulle.

### Tri

Dans les deux boucles précédentes, les valeurs affichées à l'écran pourraient être affichées dans un ordre différent à chaque fois que le programme est exécuté.

Si on a besoin d'un ordre spécifque, il faut le spécifier.

```swift title="Swift"
let cles = Array(monDictionnaire.keys).sorted()
```

ou encore :

```swift title="Swift"
let monDictionnaireTrie = monDictionnaire.sorted(by: <)
```

### Quelques méthodes utiles

- [allSatisfy()](https://developer.apple.com/documentation/swift/dictionary/allsatisfy(_:))
- [contains()](https://developer.apple.com/documentation/swift/dictionary/contains(where:))
- [count()](https://developer.apple.com/documentation/swift/dictionary/count)
- [filter()](https://developer.apple.com/documentation/swift/dictionary/filter(_:))
- [firstIndex()](https://developer.apple.com/documentation/swift/array/firstindex(where:))
- [forEach()](https://developer.apple.com/documentation/swift/dictionary/foreach(_:))
- [index()](https://developer.apple.com/documentation/swift/dictionary/index(forkey:))
- [isEmpty()](https://developer.apple.com/documentation/swift/dictionary/isempty)
- [keys()](https://developer.apple.com/documentation/swift/dictionary/keys-swift.property)
- [max()](https://developer.apple.com/documentation/swift/dictionary/max(by:))
- [min()](https://developer.apple.com/documentation/swift/dictionary/min(by:))
- [randomElement()](https://developer.apple.com/documentation/swift/dictionary/randomelement())
- [remove()](https://developer.apple.com/documentation/swift/dictionary/remove(at:))
- [removeValue()](https://developer.apple.com/documentation/swift/dictionary/removevalue(forkey:))
- [values()](https://developer.apple.com/documentation/swift/dictionary/values-swift.property)

??? info "Pour plus d'information"

    « Dictionary ». Apple. <https://developer.apple.com/documentation/swift/dictionary>

    « Collection Types - Dictionnaries ». Swift. <https://docs.swift.org/swift-book/LanguageGuide/CollectionTypes.html#ID113>

    « Expression implicitly coerced from ‘String?’ to ‘Any’- WHY SWIFT, WHY :( ». Steven Curtis. <https://stevenpcurtis.medium.com/expression-implicitly-coerced-from-string-to-any-why-swift-why-190dd0a58c58>

    « Dictionaries in SwiftDictionaries in Swift ». Andy Bargh. <https://andybargh.com/dictionaries-in-swift/>

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

## Structure vs classe

Swift propose des [structures](tableaux-dictionnaires-structures-et-classes.md#les-structures) et des [classes](../complements/le-langage-swift-reference.md#les-classes) pour représenter des données et des comportements.

La différence entre les deux n'est pas si évidente à prime abord.

Voici d'abord quelques ressemblances :

- Les deux permettent de définir des propriétés et des méthodes.
- Il est possible de créer des instances de structures et des instances de classes (dans le cas des classes, les instances sont aussi appelées **objets**).

Et quelques différences :

- Les classes offrent des fonctionnalités supplémentaires, par exemple l'héritage.
- Les structures, quant à elles, offrent l'avantage d'être moins complexes à mettre en oeuvre.
- Les structures ont un constructeur par défaut mais les classes n'en ont pas.
- Lorsqu'une fonction reçoit en paramètre une instance d'une classe, le paramètre est passé par référence. Quand le paramètre est une instance d'une structure, il est passé par valeur.

Pour vous aider à choisir entre créer une structure ou créer une classe, rappelez-vous qu'il faut d'abord privilégier les structures et choisir les classes seulement losrque requis[1](https://docs.swift.org/swift-book/LanguageGuide/ClassesAndStructures.html#:~:text=As%20a%20general%20guideline):,

> As a general guideline, prefer structures because they’re easier to reason about, and use classes when they’re appropriate or necessary.

### Source

1. «  Structures and Classes  ». Swift. [https://docs.swift.org/swift-book/LanguageGuide/ClassesAndStructures.html](https://docs.swift.org/swift-book/LanguageGuide/ClassesAndStructures.html#:~:text=As%20a%20general%20guideline)

## Les structures

Les [structures](https://docs.swift.org/swift-book/LanguageGuide/ClassesAndStructures.html) Swift permettent de représenter des données complexes ainsi que des comportements.

Dans SwiftUI, une structure sera généralement placée dans son propre fichier. Le nom de la structure sera identique au nom du fichier.

Puisque les structures représentent les données de l'application (le modèle), leurs fichiers seront placés dans un dossier nommé `Models`.  
  
Le nom de la structure sera un mot au singulier.

### Définir une structure

Dans la structure, les propriétés sont définies avec le mot-clé `var` et les méthodes, avec le mot-clé `func`.

```swift title="Models/Ami.swift"
import Foundation

struct Ami {
  var nomFamille: String
  var prenom: String

  func inviter() {
    ...
  }
}
```

### Instancier une structure

Pour créer une instance de la structure, on procédera comme suit :

```swift title="Swift"
let ami = Ami(nomFamille: "Wilco", prenom: "Roger")
```

Dans cet exemple, il ne sera pas possible de modifier les propriétés de l'instance puisqu'elle a été créée avec le mot-clé `let`.

### Constructeur

Chaque structure contient un constructeur par défaut, qu'on appelle en anglais **memberwise initializer**. Il n'y a rien à coder pour que ce constructeur existe. Il est là de base.

Le **memberwise initializer** permet d'instancier la structure en précisant une valeur pour chacune des propriétés, comme dans l'exemple précédent.

Il est possible de définir un constructeur nommé `init()` qui répondra à nos besoins de façon plus précise, par exemple en donnant une valeur par défaut à certaines propriétés ou en effectuant un traitement particulier.

!!! warning "Attention"
    sans précaution, ceci écrasera le **memberwise initializer**. C'est pourquoi il est préférable de créer une [extension](https://docs.swift.org/swift-book/LanguageGuide/Extensions.html) de la structure dans laquelle le ou les constructeurs seront définis.

De cette façon, l'instance pourra être créée à l'aide du **memberwise initializer** ou d'un des constructeurs définis dans l'extension.

Dans un projet SwiftUI, les extensions peuvent être placées à différents endroits selon la structure de fichiers dont vous vous êtes dotés. Dans le cas d'une extension à une structure que vous avez créée, il est intéressant de la placer dans le même fichier que la structure.

```swift title="Fichier Models/Ami.swift"
extension Ami {
  init(prenom: String) {
    self.prenom = prenom
    self.nomFamille = ""
  }
 }
```

Désormais, pour instancier un Ami, il est possible de fournir seulement le prénom.

Le nom de famille pourra être ajusté au besoin par une instruction séparée.

```swift title="Swift"
var ami = Ami(prenom: "Roger")
...
ami.nomFamille = "Wilco"
```

Tout constructeur doit s'assurer que chacune des propriétés a une valeur valide lorsque l'instanciation est terminée.

## Les propriétés calculées

Dans une classe ou dans une structure, il est possible de définir des propriétés calculées, c'est-à-dire des propriétés dont la valeur est calculée à partir d'autres valeurs.

```swift title="Swift"
class Eleve {
  var prenom: String
  var nomFamille: String

  // propriété calculée
  var nomComplet: String {
    self.prenom + " " + self.nomFamille
  }
}
```

La propriété calculée peut obtenir une valeur différente selon une condition. À ce moment, il faut utiliser le mot-clé `return` pour définir sa valeur.

```swift title="Swift"
class Eleve {
  var prenom: String
  var nomFamille: String
  var gentile: String?

  // propriété calculée
  var nomEtGentile: String {
    if self.gentile != nil {
      return self.prenom + " " + self.nomFamille + " de " + self.gentile
    }
    else {
      return self.prenom + " " + self.nomFamille
    }
  }
}
```

Voici un autre exemple de propriétés calculées, cette fois dans une vue.

```swift title="Swift"
struct AjouterItem: View {
  @State private var nom: String = ""
  ...

  // propriété calculée
  var messageNom: String {
    var message = ""
    if nom.count == 0 {
      message = "Le nom est requis."
    }
    else if nom.count > 100 {
      message = "Le nom doit comporter au maximum 100 caractères."
    }

    return message
  }

  // propriété calculée
  var formulaireValide: Bool {
    messageNom == "" && messageDescription == ""
  }

  ...

 }
```

??? info "Pour plus d'information"

    « Properties ». Swift. <https://docs.swift.org/swift-book/documentation/the-swift-programming-language/properties/>

    « What is a Computed Property in Swift? ». Swift Lee. <https://www.avanderlee.com/swift/computed-property/>

    « What are computed properties in Swift and when should you use them? ». Donny Wals. <https://www.donnywals.com/what-are-computed-properties-in-swift-and-when-should-you-use-them/>

    « Deciding between a computed property and a function in Swift ». Donny Wals. <https://www.donnywals.com/deciding-between-a-computed-property-and-a-function-in-swift/>
