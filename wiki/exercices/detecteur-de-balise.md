# Exercice 15 : Détecteur de balise de proximité

Pour cet exercice, nous allons adopter une approche différente de ce que nous avons fait jusqu'ici.

Afin de vous aider à bien saisir tout ce que l'utilisation de capteurs implique, je vous propose de suivre un tutoriel vidéo. Il n'y a pas énormément de code et quelques concepts ne vous sembleront pas si faciles à comprendre mais à la fin de cette première expérience, vous aurez tout de même une application fonctionnelle.

Vous devez travailler dans un nouveau projet Xcode.

Cette application permet de détecter si une [balise de proximité](../lecons/les-balises-de-proximite-beacons.md) est loin, près ou carrément ici.

1. Suivez le tutoriel disponible à l'adresse <https://www.youtube.com/watch?v=lCNpEaZiKqU>. N'oubliez pas de citer la source dans l'en-tête de vos fichiers.

    Dans le tutoriel, vous devez apporter quelques modifications dues à la version de SwiftUI qui est moins récente que la vôtre :

    1. Dans la structure `ContentView`, `.edgesIgnoringSafeArea(.all)` est maintenant `.ignoresSafeArea()`.

        ```swift title="SwiftUI"
        Text("UNKNOWN")
          ...
          .ignoresSafeArea()
        ```

    2. Dans la classe `BeaconDetector`, `BindableObject` est maintenant remplacé par la macro `@Observable`.

        ```swift title="SwiftUI"
        @Observable
        class BeaconDetector: NSObject, CLLocationManagerDelegate
        {
        ```

    3. Dans la classe `BeaconDetector`, la méthode `locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {...}` est obsolète. Il faut maintenant faire ceci :

        ```swift title="SwiftUI"
        func locationManagerDidChangeAuthorization(_ manager: CLLocationManager) {
          if manager.accuracyAuthorization == .fullAccuracy {
            ...    // conserver les lignes de code qui étaient dans if status == .authorizedWhenInUse
          }
        }
        ```

    4. Puisque nous avons utilisé `@Observable` au lieu de `BindableObject`, il faut remplacer dans le `ContentView` `@ObjectBinding` par `@State`.

        ```swift title="SwiftUI"
        @State private var detector = BeaconDetector()
        ```

    5. Dans le contexte du code présenté, il ne faut plus ajouter le `return` devant les `Text`.

        ```swift title="SwiftUI"
        Text("ICI")  // plutôt que return Text("ICI")
        ```

    6. La technique pour ajouter une clé dans Info.plist a également changé. Référez-vous à la fiche [Ajouter une paire clé-valeur dans Info.plist](../lecons/info-plist.md).

2. Demandez à votre IA favorite de vous expliquer pourquoi il y a des double-parenthèses dans l'instruction `didChange.send(())`.
3. Lancez votre application dans le simulateur pour vous assurer que tout fonctionne et que vous n'avez pas d'avertissement de clé manquante dans Info.plist.
4. Activez un beacon réel ou simulé. Faites le nécessaire pour que le UUID et les valeurs major et minor que l'application utilise correspondent à celles du beacon.
5. Lancez maintenant l'application sur un iPhone et constatez les changements quand vous déplacez le téléphone plus ou moins loin du beacon.
6. Éteignez le beacon. Votre application devrait maintenant indiquer que la distance du beacon est inconnue.
7. **OPTIONNEL** : en équipe de 2, 3 ou 4 personnes :
    1. Configurez chacune de vos applications qui simulent un beacon pour qu'elles aient toutes le même UUID, le même major et chacune leur valeur pour minor.
    2. Ajustez l'application qui détecte les beacons pour qu'elle scanne tous les beacons qui utilisent cet UUID, peu importe les valeurs de major et de minor. Ceci est réalisé en ne précisant aucune valeur pour major ni pour minor lors de la définition de la contrainte.

        ```swift title="SwiftUI"
        let constraint = CLBeaconIdentityConstraint(uuid: "...")
        ```

    3. La classe `BeaconDetector` retiendra la valeur du minor le plus près qu'elle détecte.

        ```swift title="SwiftUI"
        if let beacon = beacons.first {
          ...
          minorDetecte = beacon.minor.uint16Value
        ```

    4. L'application doit maintenant afficher à l'écran la valeur du minor du beacon le plus près, ou encore une chaîne qui indique clairement quel beacon est le plus près. Testez votre application en vous déplaçant près de l'un ou l'autre des simulateurs de beacon.
