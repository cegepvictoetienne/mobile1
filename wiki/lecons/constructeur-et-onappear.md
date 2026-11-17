# Constructeur et onAppear()

## init()

Une partie du travail d'initaliation d'une structure, par exemple la structure ContentView, peut être effectué [dans un constructeur](tableaux-dictionnaires-structures-et-classes.md#les-structures).

En Swift, le constructeur s'appelle `init()`.

Il s'agit d'un excellent endroit pour effectuer des tâches initiales, par exemple donner une valeur à des variables locales, à des variables d'état ou même à des constantes qui n'ont reçu aucune valeur lors de leur déclaration.

```swift title="SwiftUI"
struct ContentView: View {
  var uneVariable: String
  let uneConstante: String
  @State private var uneVariableDEtat: String

  init() {
    uneVariable = "Un"
    uneConstante = "Deux"
    uneVariableDEtat = "Trois"
  }

  var body: some View {
    VStack {
      Text(uneVariable)   // affiche Un
      Text(uneConstante)   // affiche Deux
      Text(uneVariableDEtat)   // affiche Trois
    }
  }
}
```

### Cas des variables d'état

L'initialisation de variable d'état dans le `init()` pourrait poser problème dans certaines circonstantes. Il faudra à ce moment vous tourner vers [.onAppear()](constructeur-et-onappear.md#onappear) pour effectuer le travail.

Le problème se posera notamment lorsque **toutes** les propriétés ont déjà reçu une valeur lors de leur déclaration.

```swift title="SwiftUI"
struct ContentView: View {
  var premierTexte: String = "déclaration"
  @State private var deuxiemeTexte: String = "déclaration"

  init() {
    premierTexte = "initialisation"   // cette ligne est toujours prise en compte car pas variable d'état
    deuxiemeTexte = "initialisation"   // si toutes les propriétés ont reçu une valeur à la déclaration, cette ligne n'est pas prise en compte
  }

  var body: some View {
    VStack {
      Text(premierTexte)   // affiche initialisation
      Text(deuxiemeTexte)   // affiche déclaration
    }
    .padding()
  }
}
```

## .onAppear()

Puisque la vue est une structure, il est possible d'effectuer une partie du travail d'initalisation [en définissant un constructeur](constructeur-et-onappear.md#init).

Le travail du constructeur survient très tôt dans le cycle de vie d'une application SwiftUI. Pour cette raison, certaines opérations d'initialisation ne peuvent pas être réalisées dans le constructeur.

### onAppear()

La méthode [onAppear()](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) est un endroit intéressant pour effectuer le travail d'initialisation puisque le code qu'elle contient sera exécuté beaucoup plus tard dans le cycle de vie, juste avant que la vue soit affichée.

```swift title="SwiftUI"
var body: some View {
  ...   // vue à laquelle onAppear est rattaché
  .onAppear(perform: {
    maFonction()
  })
}

func maFonction() {
  maVariableDEtat = "une valeur"
  ...
}
```

Dans le cas où la fonction à exécuter ne reçoit aucun paramètre, il est possible de simplifier la syntaxe en enlevant les accolades dans `.onAppear` de même que les parenthèses à la fonction.

```swift title="SwiftUI"
var body: some View {
  ...   // vue à laquelle onAppear est rattaché
  .onAppear(
    perform: maFonction
  )
}

func maFonction() {
  maVariableDEtat = "une valeur"
  ...
}
```

### Pour plus d'information

« SwiftUI View Lifecycle ». vadimbulavin.com. <https://www.vadimbulavin.com/swiftui-view-lifecycle/>

« Running Code Only Once in SwiftUI ». https://www.swiftjectivec.com/. <https://www.swiftjectivec.com/swiftui-run-code-only-once-versus-onappear-or-task/>
