# Notification à l'aide d'une vibration

Dans une application SwiftUI, il est intéressant de générer une rétroaction physique ([playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics)) telle une vibration.

Fait intéressant : si vous travaillez avec le modifieur [.sensoryFeedback()](https://developer.apple.com/documentation/SwiftUI/SensoryFeedback), le système se chargera d'ignorer la vibration si l'appareil mobile ne supporte pas cette fonctionnalité.

Notez que certaines vibrations requièrent que les vibrations système soient activées sur le téléphone : **Réglages** / **Sons et vibrations** / **Vibrations système**.

C'est pourquoi la vibration ne doit pas être la seule source de rétroaction à l'usager. Elle doit être complémentaire à une modification du visuel, par exemple l'affichage d'un message, un changement de couleur, etc.

## Types de vibration

Il existe différents types de vibration à utiliser dans un contexte précis.

Il faut respecter autant que possible les standards afin de ne pas « dénaturer » la signification de la vibration.

### Succès, avertissement, erreur

L'application peut utiliser une vibration standard pour signifier, par exemple, une réussite, un avertissement ou un échec.

L'utilisation de [SensoryFeedback](https://developer.apple.com/documentation/SwiftUI/SensoryFeedback) rend l'ajout de vibration très simple. Ce modifieur prend deux paramètres :

- le type de vibration (ex : .success, .warning, .error)
- le déclencheur

La vibration se produira dès que la valeur du déclencheur change.

Dans cet exemple, il y aura une vibration d'avertissement dès que la variable `vibrationAvertissement` change de valeur.

```swift title="SwiftUI"
struct ContentView: View {
  @State private var vibrationAvertissement: Bool = false

  var body: some View {
    VStack {
      ...
      Button(action: {
        ...
        if ... {
          vibrationAvertissement.toggle()   // ceci déclenchera la vibration
        }
      }) {
        Text("Faire quelque chose")
      }
    }
    .sensoryFeedback(.warning, trigger: vibrationAvertissement)
  }
}
```

Voici un exemple qui émet une vibration de succès ou d'échec selon le cas. Remarquez la différence de syntaxe pour qu'un seul modifieur émette un type de vibration différent selon le contexte.

```swift title="SwiftUI"
struct ContentView: View {
  @State private var succes: Bool = false
  @State private var declencheur: Int = 0

  var body: some View {
    VStack {
      Button(action: {
        succes = true
        declencheur += 1   // la valeur du déclencheur doit être modifiée pour lancer la vibration
      }) {
        Text("Succès")
      }

      Button(action: {
        succes = false
        declencheur += 1
      }) {
        Text("Succès")
       }
    }
    .sensoryFeedback(trigger: declencheur) { _, _ in
      succes ? .success : .error
    }
  }
}
```

 Astuce : si vous devez faire une vidéo qui démontre l'utilisation de la vibration, le fait de placer le téléphone sur une cannette vide permettra d'entendre la vibration.
