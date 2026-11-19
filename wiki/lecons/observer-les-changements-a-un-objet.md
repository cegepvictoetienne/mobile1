# @Observable

La notion d'observation avec SwiftUI permet à une vue de surveiller un objet et d'être automatiquement mise à jour lorsqu'une de ses propriétés change. Ce mécanisme est similaire à la notion d'écouteur (**listener**) dans d'autres langages de programmation.

## Rendre une classe observable

Pour qu'une classe soit observable, il suffit de la décorer avec la macro `@Observable`.

Dans cet exemple, les vues qui utilisent un objet de cette classe seront avisées des changements que la classe apporte aux propriétés `valeur` et ***message*** de l'objet.

```swift title="SwiftUI"
@Observable
class MaClasseObservable {
  var valeur: Double = 0.0
  var message: String = ""
  ...
}
```

## Exclure une propriété de l'observation

Par défaut, toutes les propriétés de la classe seront observables.

Il est possible d'exclure certaines propriétés du mécanisme d'observation en les décorant avec la macro [@ObservationIgnored](https://developer.apple.com/documentation/Observation/ObservationIgnored()). Ceci est utile pour des propriétés internes qui n'ont pas d'impact sur l'interface.

Ici, l'objet `uneProprieteObjet` n'a pas à être observé. Les vues qui utilisent la classe travailleront seulement avec `valeur` et ***message***.

```swift title="SwiftUI"
@Observable
class MaClasseObservable {

  @ObservationIgnored
  private var uneProprieteObjet = UneClasse()

  var valeur: Double = 0.0
  var message: String = ""
   ...
}
```

## Utiliser un objet observable dans une vue

Pour qu'une vue réagisse aux changements d'un objet observable, il faut déclarer cet objet avec `@State`. C'est le combinaison de `@Observable` sur la classe et de `@State` sur la variable qui rend la vue réactive.

```swift title="SwiftUI"
struct ContentView: View {
  @State private var objetDeMaClasseObservable: MaClasseObservable = MaClasseObservable()

  var body: some View {
    VStack {
      // la vue sera rafraîchie dès qu'une propriété observable accédée dans le body change
      Text("Valeur: \(objetDeMaClasseObservable.valeur)")
      Text("Message: \(objetDeMaClasseObservable.message)")
    }
  }
}
```

Note : il est aussi possible d'utiliser `@Bindable` plutôt que `@State` afin de permettre à la vue enfant de modifier la variable à l'aide d'une vue qui requiert une liaison, par exemple `TextField`.

## Avant iOS 17

La macro `@Observable` n'existe que depuis iOS 17, sorti en septembre 2023.

Auparavant, le mécanisme d'observation était réalisé à l'aide de [ObservableObject，@Published et @StateObject](fonctions-obsoletes-ou-anciennes-syntaxes.md#observableobject-published-et-stateobject).

L'ancien mécanisme fonctionne toujours mais lorsqu'on développe pour iOS 17 ou plus récent, on préférera travailler avec la macro `@Observable` puisqu'elle est plus simple à mettre en oeuvre. De plus, `@Observable` est plus performant grâce à la compilation des macros.

??? info "Pour plus d'information"

    « Migrating from the Observable Object protocol to the Observable macro ». Apple. <https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro>
