# Les boucles

## Boucle for

La [boucle for](https://docs.swift.org/swift-book/LanguageGuide/ControlFlow.html#ID121) en langage Swift permet d'effectuer une boucle.

Elle ressemble beaucoup à la structure de contrôle du même nom dans d'autres langages, par exemple PHP ou JavaScript.

C'est une bonne habitude à prendre de donner un nom au pluriel à la variable qui stocke les éléments. Ceci permet d'utiliser ce même mot au singulier pour identifier l'élément qui est actuellement traité.

```swift title="Swift"
for valeur in valeurs {
  print(valeur)
}
```

## forEach()

Dans le langage Swift, la méthode [forEach()](https://developer.apple.com/documentation/swift/array/foreach(_:)) permet de boucler sur les éléments d'une collection.

Après l'accolade ouvrante, on spécife le nom que portera l'élément de la collection qui est actuellement traité, suivi du mot-clé `in`.

```swift title="Swift"
monTableau.forEach { element in
  print(element)
}
```

Si vous désirez boucler un nombre défini de fois, vous pouvez utiliser cette syntaxe :

```swift title="Swift"
(0...4).forEach { i in
  print(i)
}
```

## ForEach()

La structure [ForEach()](https://developer.apple.com/documentation/swiftui/foreach) de SwiftUI permet de créer une vue à partir des éléments d'une collection.

Elle ressemble à [la méthode forEach()](les-boucles.md#foreach) à première vue mais détrompez-vous, il s'agit de deux choses différentes.

Les deux permettent de boucler sur une collection, c'est vrai. Mais alors que `forEach()` est une méthode, `ForEach()` est une vue.

C'est pourquoi seule la structure `ForEach()` permet de boucler pour créer plusieurs instances d'un Text, d'un TextField, d'une image, etc.

Par exemple, ceci permet de créer une image pour chaque image dont le nom est stocké dans un tableau de String.

```swift title="SwiftUI"
let photos = ["grand-boss", "petit-boss", "employe", "trou-de"]
...
ForEach(photos, id: \.self) { photo in
  Image(photo)
    .resizable()
    .scaledToFit()
 }
```

Autre exemple, pour créer 5 cases de saisie liées à chacun des éléments d'un tableau de String :

```swift title="SwiftUI"
@State private var noms = Array(repeating: "", count: 5)
...
ForEach((0...4), id: \.self) { i in
  TextField("", text: $noms[i])
}
```

### Paramètre id

Vous vous demandez probablement à quoi sert le paramètre nommé `id`.

Il est requis pour permettre à SwiftUI d'identifier chaque élément de façon unique.

Ici, on utilise `\.self`, c'est-à-dire un hash que Swift produit pour identifier l'élément actuellement traité.

### Tableau d'instances d'une structure

Prenons le cas où l'application travaille avec cette structure :

```swift title="Fichier Models/Item.swift"
struct Item {
  var code: String
  var titre: String
}
```

Pour utiliser un `ForEach` avec le paramètre `id: \.self`, il faudrait que la structure réponde au protocole `Hashable`, ce qui n'est pas le cas ici.

```swift title="Swift"
ForEach(items, id: \.self) { item in
  Text(item.titre)
}
```

Si vous devez utiliser un tel tableau sans modifier la structure, vous devez absolument avoir un champ dont la valeur est unique, par exemple le code de l'item.

```swift title="Swift"
ForEach(items, id: \.code) { item in
  Text(item.titre)
}
```

Si deux items avaient le même code, l'application pourrait avoir un comportement erratique.

### Protocole Identifiable

Si la collection utilisée dans la boucle répond au protocole [Identifiable](https://developer.apple.com/documentation/swift/identifiable), la boucle `ForEach` sera plus simple puisque SwiftUI saura automatiquement comment identifier chaque élément de façon unique.

```swift title="Fichier Models/Item.swift"
struct Item: Identifiable {
  var id: Int
  var code: String
  var titre: String
}
```

Maintenant, pour boucler dans un tableau d'instances de cette structure :

```swift title="SwiftUI"
ForEach(items) { item in
  Text(item.titre)
}
```

### Tentatives avec autres boucles

Si vous tentez d'utiliser un autre type de boucle pour produire la vue, par exemple une boucle `for`, vous obtiendre le message d'erreur « Closure containing control flow statement cannot be used with result builder 'ViewBuilder' ».

Et si vous tentez le coup avec la méthode `forEach()`, vous pourriez obtenir un message du genre « The compiler is unable to type-check this expression in reasonable time; try breaking up the expression into distinct sub-expressions ».

??? info "Pour plus d'information"

    « Why does \.self work for ForEach? ». Hacking with Swift. <https://www.hackingwithswift.com/books/ios-swiftui/why-does-self-work-for-foreach>

## Modifier l'élément présentement traité dans une boucle

Par défaut, quand une vue fait une itération pour afficher les éléments d'un tableau, par exemple avec [List](quelques-vues-swiftui.md#list) ou avec [ForEach](les-boucles.md#foreach_1), le code à l'intérieur de la boucle ne peut pas modifier les éléments du tableau.

Si vous tentez de faire une telle modification, vous aurez un message d'erreur du genre « Cannot assign to property: 'item' is a 'let' constant ».

```swift title="SwiftUI"
ForEach(items) { item in
  ...
  Button("Activer") {
    item.actif = true
  }
 }
```

Si vous avez réellement le besoin d'effectuer une telle modification, il est possible d'y arriver en ajoutant un **Binding** au tableau ainsi qu'au nom du paramètre.

```swift title="SwiftUI"
ForEach($items) { $item in
  ...
  Button("Activer") {
    item.actif = true
  }
 }
```

Autre technique : boucler sur les indices plutôt que sur le tableau directement. Mais attention : avec cette technique, l'application pourrait planter si la taille du tableau était modifiée pendant que la vue se met à jour.

```swift title="SwiftUI"
ForEach(items.indices, id: \.self) { index in
  ...
  Button("Activer") {
    items[index].actif = true
  }
}
```

??? info "Pour plus d'information"

    « How to create a List or a ForEach from a binding ». Hacking with Swift. <https://www.hackingwithswift.com/quick-start/swiftui/how-to-create-a-list-or-a-foreach-from-a-binding>
