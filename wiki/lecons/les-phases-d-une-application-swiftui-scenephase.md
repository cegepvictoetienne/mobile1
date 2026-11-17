# Réagir quand l'application devient active ou inactive

Dans le fichier principal de l'application (ex : MonProjetApp.swift), le code initial du projet SwiftUI déclare une propriété `body` qui retourne on objet de type [Scene](https://developer.apple.com/documentation/swiftui/scene).

```swift title="Fichier MonProjetApp.swift"
import SwiftUI

@main
struct MonProjetApp: App {
  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}
```

Il est possible de déterminer dans quelle phase cette scène se trouve et d'effectuer les opérations pour que l'application demeure cohérente dans ces différentes phases.

Nous utliserons pour cela la propriété [scenePhase](https://developer.apple.com/documentation/swiftui/environmentvalues/scenephase).

```swift title="Fichier MonProjetApp.swift"
import SwiftUI

@main
struct MonProjetApp: App {

  @Environment(\.scenePhase) private var scenePhase

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
    .onChange(of: scenePhase) { phase in
      switch phase {
      case .active:
        ...
      case .inactive:
        ...
      case .background:
        ...
      @unknown default:
        ...
      }
    }
  }
}
```

Il est également possible de vérifier la phase d'une vue en particulier.

```swift title="Fichier MonProjetApp.swift"
import SwiftUI

struct MaVue: View {

  @Environment(\.scenePhase) private var scenePhase

  var body: some View {
    VStack {
      ...
    }
    .onChange(of: scenePhase) { phase in
      switch phase {
      case .active:
        ...
      case .inactive:
        ...
      case .background:
        ...
      @unknown default:
        ...
      }
    }
  }
}
```

## Pour plus d'information

« Using Core Data with SwiftUI App Protoc ». Apple Developer Forums. <https://developer.apple.com/forums/thread/650876?answerId=620207022#620207022>
