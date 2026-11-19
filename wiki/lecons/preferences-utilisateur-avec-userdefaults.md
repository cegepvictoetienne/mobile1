# Enregistrement de données simples avec UserDefaults

La classe [UserDefaults](https://developer.apple.com/documentation/foundation/userdefaults) est spécifiquement conçue pour enregistrer des paires clé-valeur, par exemple des préférences utilisateur.

Dans les faits, il est souvent préférable de travailler avec l'attribut [@AppStorage](les-preferences-utilisateur.md#appstorage) car son utilisation est plus intuitive.

Si vous êtes curieux d'en savoir plus, je vous explique ici le fonctionnement de `UserDefaults`, la classe qui se cache sous `@AppStorage`.

## UserDefaults.standard

Dans la classe `UserDefaults`, la variable de classe `standard` permet d'accéder aux paires clé-valeur.

Il est possible de travailler avec une variable locale pour y accéder mais ceci n'est pas une obligation.

```swift title="SwiftUI"
struct ContentView: View {
  let mesDonneesUtilisateur = UserDefaults.standard
  ...
  mesDonneesUtilisateur.set("ma valeur", forKey: "maCle")
}
```

Si vous ne créez pas une telle variable, vous devrez spécifier `UserDefaults.standard` à chaque fois que vous désirez accéder aux paires clé-valeur.

```swift title="SwiftUI"
UserDefaults.standard.set("ma valeur", forKey: "maCle")
```

## Enregistrer une paire clé-valeur

La méthode [set()](https://developer.apple.com/documentation/foundation/userdefaults/1414067-set) permet de d'enregistrer une valeur pour une clé.

```swift title="SwiftUI"
mesDonneesUtilisateur.set("ma valeur", forKey: "maCle")
```

ou :

```swift title="SwiftUI"
UserDefaults.standard.set("ma valeur", forKey: "maCle")
```

Il est possible d'enregistrer une multitude de types de données, par exemple une chaîne simple, une chaîne JSON, un nombre, un booléen, un tableau, un dictionnaire.

## Retrouver la valeur enregistrée pour une clé

Pour lire la valeur enregistrée pour une clé, il est possible d'utiliser une méthode qui correspond au type de la donnée : [string(forKey:)](https://developer.apple.com/documentation/foundation/userdefaults/1416700-string), [bool(forKey:)](https://developer.apple.com/documentation/foundation/userdefaults/1416388-bool), [integer(forKey:)](https://developer.apple.com/documentation/foundation/userdefaults/1407405-integer), etc.

Il faut toujours tenir compte du fait que la clé pourrait ne pas exister.

On utilisera l'[opérateur de fusion nil](https://docs.swift.org/swift-book/LanguageGuide/BasicOperators.html#:~:text=Nil-Coalescing%20Operator) (**Nil-Coalescing Operator**) pour spécifier la valeur par défaut.

```swift title="Swift"
maValeur = UserDefaults.standard.string(forKey: "maCle") ?? "clé maCle inexistante"
```

La méthode [object(forKey:)](https://developer.apple.com/documentation/foundation/userdefaults/1410095-object) combinée à une conversion de type (**type cast**) peut être utilisée peu importe le type de données.

Notez que dans cet extrait, l'opérateur `as?` indique que la valeur doit être convertie au type spécifié mais qu'elle pourrait être nil.

```swift title="SwiftUI"
maValeur = UserDefaults.standard.object(forKey: "maCle") as? String ?? "clé maCle inexistante"
```

??? info "Pour plus d'information"

    « Swift Userdefaults 1/4 pour sauvegarder mais pas trop ». Medium. <https://medium.com/@luc.derosne/swift-userdefaults-1-4-pour-sauvegarder-mais-pas-trop-22d1cbe6f26>

    « The Advanced Guide to UserDefaults in Swift ». Yet Another Swift Blog. <https://www.vadimbulavin.com/advanced-guide-to-userdefaults-in-swift/>
