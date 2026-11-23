# Faire défiler l'écran

## ScrollView

La structure [ScrollView](https://developer.apple.com/documentation/swiftui/scrollview) permet de faire défiler l'écran verticalement.

Notez que certaines vue, par exemple [List](quelques-vues-swiftui.md#list), assurent le défilement donc un ScrollView n'est alors pas nécessaire.

```swift title="SwiftUI"
var body: some View {
    NavigationStack {
        ScrollView {
            VStack {
                ...
            } // fin VStack principal
        } // fin ScrollView
        .navigationTitle("Mon application")
    } // fin NavigationStack
} // fin body
```

??? info "Pour plus d'information"

    « Mastering ScrollView in SwiftUI ». Swift with Majid. <https://swiftwithmajid.com/2020/09/24/mastering-scrollview-in-swiftui/>

## Défilement infini (infinite scroll)

Information à venir...

??? info "Pour plus d'information"

    « mplementing an infinite scrolling list with SwiftUI and Combine ». Donny Wals. <https://www.donnywals.com/implementing-an-infinite-scrolling-list-with-swiftui-and-combine/>

## LazyVStack et LazyHStack

Information à venir...

??? info "Pour plus d'information"

    « How ScrollView lets us work with scrolling data ». Hacking with Swift. <https://www.hackingwithswift.com/books/ios-swiftui/how-scrollview-lets-us-work-with-scrolling-data>

    « https://www.gfrigerio.com/lazy-loading-in-swiftui/ ». Gualtiero Frigerio. <https://www.gfrigerio.com/lazy-loading-in-swiftui/>
