# Où peut-on déclarer des vues et effectuer des traitements

Lorsqu'on effectue de la programmation réactive, comme c'est le cas avec SwiftUI, il n'est pas possible de placer n'importe quel extrait de code n'importe où.

Voici quelques lignes pour vous guider.

## Modification d'une variable d'état

La valeur d'une variable d'état ne doit jamais être modifiée directement dans une vue. Le `body` d'une vue doit uniquement décrire l'interface à afficher.

La variable d'état doit plutôt être modifiée en réponse à un événement, par exemple un clic sur un bouton.

Si vous tentez de modifier une variable d'état directement dans une vue, vous obtiendrez un message du genre : `Type '()' cannot conform to 'View'`{ .erreur }.

```swift title="SwiftUI"
struct ContentView: View {
  @State private var nom: String = ""

  var body: some View {
    VStack {
      nom = "Roger"
      Text(nom)
      ...
    }
  }
}
```

Cet exemple permet de modifier correctement la variable d'état.

```swift title="SwiftUI"
Button(action: {
  nom = "Roger"
 }) {
  Text("Modifier le nom")
 }
 .buttonStyle(.bordered)
```

## Déclaration d'une vue

Toutes les vues doivent être déclarées dans le corps principal de `ContentView` ou de ses enfants.

Il n'est pas possible de déclarer une vue en réaction à un événement.

Si vous le faites, vous pourriez obtenir une erreur ou un avertissement du compilateur, par exemple `Result of 'Text' initializer is unused`{ .erreur } et vous n'obtiendrez pas le résultat escompté.

```swift title="SwiftUI"
struct ContentView: View {
  @State private var nom: String = "Roger"

  var body: some View {
    VStack {
      Button(action: {
        Text(nom)
      }) {
        Text("Afficher le nom")
      }
      .buttonStyle(.bordered)
    }
  }
}
```

Il faut plutôt ajouter un `if` dans le `body` pour que le nom soit affiché selon une condition.

Ici, le nom sera affiché seulement après avoir cliqué sur le bouton.

```swift title="SwiftUI"
struct ContentView: View {
  @State private var nom: String = "Roger"
  @State private var afficherNom: Bool = false

  var body: some View {
    VStack {
      Button(action: {
        afficherNom = true
      }) {
        Text("Afficher le nom")
      }
      .buttonStyle(.bordered)

      if afficherNom {
        Text(nom)
      }
    }
  }
}
```
