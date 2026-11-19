# Transférer des informations entre les vues

## Transférer des informations de la vue parent vers une vue enfant (initialisation de propriétés)

Une vue parent peut transmettre de l'information à la vue enfant vers laquelle elle navigue.

Ceci est particulièrement intéressant dans une liste d'items qui permet d'afficher la page de détail de chaque item à partir d'une même vue enfant.

D'abord, la vue enfant définiera les propriétés dont elle a besoin.

```swift title="Fichier Views/VueDetail.swift"
struct VueDetail: View {
  var description: String
  var inventaire: Int

  var body: some View {
    ...
  }
}
```

Ensuite, la vue parent initialisera ces variables lors de l'appel de la vue enfant.

```swift title="SwiftUI"
NavigationLink(destination: VueDetail(description: "Item XYZ", inventaire: 36)) {
  Text("Item XYZ")
}
```

??? info "Pour plus d'information"

    « View Communication Patterns in SwiftUI ». Vadim Bulavin. <https://www.vadimbulavin.com/passing-data-between-swiftui-views/>

## De la vue enfant vers la vue parent (@Binding et @Bindable))

Une vue enfant peut récolter des informations qu'elle doit rendre à la vue parent.

### Variable d'état créée dans la vue parent

Voici comment le transfert d'informations se déroulera.

Lorsqu'une variable est déclarée avec l'attribut [@Binding](https://developer.apple.com/documentation/swiftui/binding) (en anglais, on dit que c'est un **property wrapper**), ceci indique que la variable appartient à la vue parent mais qu'elle peut être modifiée autant par la vue parent que par la vue enfant. Il s'agit d'une liaison bidirectionnelle.

Le parent la transmet à l'enfant en la faisant précéder par le signe `$`.

```swift title="Vue parent (SwiftUI)"
struct VueParent: View {
  @State private var maVariable: String = "valeur initiale"   // la variable appartient à cette vue

  var body: some View {
    NavigationStack {
      VStack {
        Text(maVariable)
          .padding()
        NavigationLink(destination: VueEnfant(etat: $maVariable)) {
          Text("Vue enfant")
        }
      }
    }
  }
}
```

```swift title="Vue enfant (SwiftUI)"
struct VueEnfant: View {
  @Binding var etat: String   // la variable appartient à la vue parent et elle peut être modifiée ici

  var body: some View {
    Button("Changer la valeur") {
      etat = "valeur modifiée"   // cette valeur affectera maVariable dans la vue parent
    }
  }
}
```

 Le résultat de cette application de démonstration n'est pas esthétique mais on y voit bien le fonctionnement du @Binding.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Voici la vue parent avant d'afficher la vue enfant. |  | La vue enfant contient un bouton qui permet de modifier la valeur de la variable du parent. |  | Voici à nouveau la vue parent après que l'usager ait cliqué sur le bouton dans la vue enfant. |
| Avant de cliquer sur le bouton |  | Avant de cliquer sur le bouton |  | Après avoir cliqué sur le bouton |

### Variable observable sans liaison

Une variable est observable dans différentes situations, par exemple :

- une propriété d'une classe ou structure décorée avec `@Observable`
- une variable dont les valeurs sont tirées de la base de données grâce à SwiftData et `@Query`

Lorsqu'une variable est observable, les modification qui lui sont apportées se reflètent automatiquement partout dans l'application.

Une vue enfant peut travailler avec cette variable, qu'elle recevra en paramètre.

```swift title="Vue parent (SwiftUI)"
struct VueParent: View {
  @Query(sort: \Item.code) var items: [Item]   // la variable est observable

  var body: some View {
    NavigationStack {
      List(items) { item in
        VStack(alignment: .leading) {
          HStack {
            Text("\(item.code) - \(item.titre)")
            Spacer()
            NavigationLink(destination: VueEnfant(unItem: item)) {   // pas besoin de $ devant le paramètre
              Image(systemName: "pencil.line")
            }
            .buttonStyle(.bordered)
            ...
          }
        }
      }
    }
  }
}
```

```swift title="Vue enfant (SwiftUI)"
struct VueEnfant: View {
  var unItem: Item

  var body: some View {
    Button("Changer la valeur") {
      item.titre = "valeur modifiée"   // l'item sera modifié partout dans l'application
     }
  }
}
```

### Variable observable avec liaison

Dans le cas où le paramètre observable doit être utilisé dans une liaison, par exemple dans un `TextField`,  il faut le décorer avec [@Bindable](https://developer.apple.com/documentation/swiftui/bindable) dans la vue enfant.

Remarquez que lorsqu'une vue enfant reçoit un paramètre décoré avec `@Bindable`, la vue parent n'a pas besoin de faire précéder le paramètre par le signe `$` lorsqu'elle appelle la vue enfant.

La vue parent sera identique au cas où la variable observable n'a pas besoin de liaison (voir ci-haut).

La vue enfant sera modifiée comme suit :

```swift title="Vue enfant (SwiftUI)"
struct VueEnfant: View {
  @Bindable var unItem: Item   // la variable est déclarée ailleurs, elle est observable et doit être utilisée dans un binding

  var body: some View {
    TextField("Nom", text: $unItem.nom)   // l'item sera modifié partout dans l'application
    ...
  }
}
```

??? info "Pour plus d'information"

    « Managing Data Flow in SwiftUI ». Swift with Majid. <https://swiftwithmajid.com/2019/07/03/managing-data-flow-in-swiftui/>

    «  What's the difference between @Bindable and @Binding?  ». Hacking with Swift. <https://www.hackingwithswift.com/quick-start/swiftdata/whats-the-difference-between-bindable-and-binding>

## Variables globales (@Environment et @EnvironmentObject)

Si l'application a besoin de passer un objet entre des vues qui ne sont pas directement liées, par exemple de la vue parent vers l'enfant de son enfant, il est possible de travailler avec l'attribut (**property wrapper**) [@Environment](https://developer.apple.com/documentation/swiftui/environment) lorsque la classe est décorée avec [@Observable](observer-les-changements-a-un-objet.md) ou [@EnvironmentObject](https://developer.apple.com/documentation/swiftui/environmentobject) si vous utilisez l'ancienne technique qui consiste à [conformer la classe au protocole ObservableObject](fonctions-obsoletes-ou-anciennes-syntaxes.md#observableobject-published-et-stateobject).

Prenons l'exemple de cette classe observable.

```swift title="Fichier MaClasse.swift"
@Observable
class MaClasse {
  var options = ["Option 1", "Option 2", "Option 3"]
  ...
}
```

Un objet de cette classe peut être injecté dans l'environnement afin d'être partagé entre plusieurs vues. Il doit être déclaré dans le plus proche parent des vues qui en ont besoin.

Dans cet exemple, l'objet est déclaré dans le ContentView.

```swift title="Fichier ContentView.swift"
struct ContentView: View {
  @State private var monObjet = MaClasse()

  var body: some View {
    NavigationStack {
      ...
      NavigationLink(destination: VueSelection()) {
        Text("Choisir une option")
      }
    }
    .environment(monObjet)
  }
}
```

La vue enfant (ou ses descendants) pourront accéder à l'objet à l'aide de `@Environment`.

```swift title="Fichier VueSelection.swift"
struct VueSelection: View {
  @Environment(MaClasse.self) var monObjet
  @State private var optionChoisie: String?

  var body: some View {
    VStack {
      ...
      HStack {
        Text("Option: ")
        Picker("", selection: $optionChoisie) {
          Text("Veuillez choisir...").tag(nil as String?)
          ForEach(monObjet.options, id: \.self) { option in
            Text(option).tag(option as String?)
          }
        }
      }
    }
  }
}
```

??? info "Pour plus d'information"

    « How to use @EnvironmentObject to share data between views ». Hacking with Swift. <https://www.hackingwithswift.com/quick-start/swiftui/how-to-use-environmentobject-to-share-data-between-views>

    « The power of Environment in SwiftUI ». Swift with Majid. <https://swiftwithmajid.com/2019/08/21/the-power-of-environment-in-swiftui/>

    « @EnvironmentObject explained for sharing data between views in SwiftUI ». SwiftLee. <https://www.avanderlee.com/swiftui/environmentobject/>
