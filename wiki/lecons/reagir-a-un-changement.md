# .onChange()

On sait que les vues peuvent être mises à jour automatiquement lors du changement de valeur pour une variable déclarée par exemple à l'aide de `@State` ou `@AppStorage`.

Mais s'il fallait, lorsqu'une variable change, effectuer une autre tâche qu'un rechargement de la vue, par exemple faire jouer un son ou une vibration ou encore laisser une trace dans la sortie standard?

Le modificateur `onChange()` est tout à fait indiqué pour ce type de travail.

## onChange()

Le modificateur [onChange()](https://developer.apple.com/documentation/swiftui/view/onchange(of:initial:_:)-4psgg) permet d'exécuter un traitement dès que la valeur d'une variable change.

Le traitement est effectué après le changement de la valeur, donc la nouvelle valeur est déjà en place lors de son exécution.

```swift title="SwiftUI"
struct ContentView: View {
  @State private var uneVariable: String = ""

  var body: some View {
    VStack {
      ...
    }
    .onChange(of: uneVariable) { ancienneValeur, nouvelleValeur in
      print(ancienneValeur)   // affiche l'ancienne valeur
      print(nouvelleValeur)   // affiche la nouvelle valeur
      ...
    }
  }
}
```

Dans le cas où le code n'a pas besoin de travailler avec l'ancienne valeur, il est possible d'utiliser cette syntaxe simplifiée :

```swift title="SwiftUI"
struct ContentView: View {
  @State private var uneVariable: String = ""

  var body: some View {
    VStack {
      ...
    }
    .onChange(of: uneVariable) {
      print(uneVariable)   // uneVariable contient déjà la nouvelle valeur
      ...
    }
  }
}
```

## Réagir au changement d'une variable qui est constamment modifiée

Si, après avoir implanté un `onChange()`, vous obtenez le message « onChange(of: Double) action tried to update multiple times per frame.  », ceci est dû au fait que la variable utilisée change de valeur trop souvent.

Pour limiter le nombre d'exécutions du `onChange()`, une astuce consiste à créer une variable calculée qui est un arrondi de l'autre variable.

```swift title="SwiftUI"
struct ContentView: View {
  @State private var uneVariable: Double = 0.0   // cette variable est très, très souvent modifiée
  var variableArrondie: Double {
    (uneVariable * 10).rounded() / 10
  }

  var body: some View {
    VStack {
      ...
    }
    .onChange(of: variableArrondie) {
      ...
    }
  }
}
```

## Réagir au changement d'une variable optionnelle

Dans le cas où la variable est optionnelle, il faut comprendre que les variables qui contiennent l'ancienne valeur et la nouvelle valeur sont également optionnelles.

Il faudra alors prendre soin de les déballer correctement.

```swift title="SwiftUI"
struct ContentView: View {
  @State private var uneVariable: String? = ""

  var body: some View {
    VStack {
      ...
    }
    .onChange(of: uneVariable) { ancienneValeur, nouvelleValeur in
      if let nouvelleValeur {
         print(nouvelleValeur)
      }
      else {
        print("La nouvelle valeur est nulle.")
      }
      ...
    }
  }
}
```

ou, de façon plus concise :

```swift title="SwiftUI"
struct ContentView: View {
  @State private var uneVariable: String? = ""

  var body: some View {
    VStack {
      ...
    }
    .onChange(of: uneVariable) { ancienneValeur, nouvelleValeur in
       print(nouvelleValeur ?? "La nouvelle valeur est nulle.")
      ...
    }
  }
}
```

## Syntaxes obsolètes

Avant iOS 17, [la syntaxe de onChange() pouvait prendre différentes formes](fonctions-obsoletes-ou-anciennes-syntaxes.md#onchange-avant-ios-17).

Ces syntaxes sont obsolètes et ne doivent plus être utilisées si on cible iOS 17 ou plus.

```swift title="SwiftUI"
.onChange(of: uneVariable, perform: { nouvelleValeur in
  ...
})
```

```swift title="SwiftUI"
.onChange(of: uneVariable, perform: { _ in
 ...
 })
```
