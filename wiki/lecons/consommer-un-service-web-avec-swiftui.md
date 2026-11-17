# Consommer un service Web avec SwiftUI

## Consommer un service Web pour synchroniser les données

La classe [URLSession](https://developer.apple.com/documentation/foundation/urlsession) permet à une application Swift de faire appel à un service Web, aussi appelé **API** (**Application Programming Interface**).

Je vous présente ici une technique pour appeler un [service Web qui permet de synchroniser des données locales avec une base de données distante](synchronisation-des-donnees-locales-dans-le-nuage.md#service-web-pour-synchroniser-les-donnees).

### Données fournies au service Web

Le service Web de mon exemple attend en entrée une représentation JSON des données à synchroniser pour une table d'items gérée par SwiftData.

Pour encoder ces données, il faut que [la classe Item réponde au protocole Encodable](conversion-json-codable-encodable-decodable.md#rendre-un-modele-swiftdata-encodable-ou-decodable).

```swift title="Swift"
@Model
final class Item: Encodable {
  ...
}
```

Il serait possible d'ajouter d'autres informations en entrée, par exemple un code d'usager et un mot de passe qui donnent accès au service Web. Il faudrait à ce moment créer une structure qui permet de stocker un tableau d'items, un code d'usager et un mot de passe tout en répondant au protocole [Encodable](https://developer.apple.com/documentation/swift/encodable).

```swift title="Swift"
struct DonneesFournies: Encodable {
  var items: [Item]
  var codeUsager: String
  var motDePasse: String
}
```

### Données retournées par le service Web

Lorsqu'on appelle un service Web, il est important de connaître le format des données retournées par ce service.

Ces données seront récupérées dans une structure qui répond au protocole [Decodable](https://developer.apple.com/documentation/swift/decodable).

```swift title="Swift"
struct ReponseDuService: Decodable {
  ...
}
```

Notez que si, dans certains contextes, **le service Web ne retourne pas certaines propriétés de la structure**, il faut les rendre optionnelles.

Sans cette précaution, le décodage ne réussira pas lorsque le service Web n'initialise pas toutes les propriétés.

```swift title="Swift"
struct ReponseDuService: Decodable {
  var erreurs: [Erreur]? = []
  ...
}
```

### À quel moment doit-on appeler le service Web de synchronisation?

Le service Web peut être appelé à différents moments, par exemple :

- lors de l'[initialisation de la vue](constructeur-et-onappear.md#onappear) (onAppear())
- en réaction à [un clic sur un bouton](quelques-vues-swiftui.md#button)
- à tous les X temps
- etc.

### Utiliser un URL non sécurisé pendant le développement

Dans cet exemple, l'application appelle un service Web sur le serveur de développement local qui débute par `http://`. L'application doit donc être configurée pour pouvoir [utiliser un URL non sécurisé](consommer-un-service-web-avec-swiftui.md#faire-appel-a-un-url-non-securise).

Une fois le développement complété, il faudra mettre le service Web en ligne et changer l'URL du service car un service qui tourne localement sur l'ordinateur ne sera pas accessible à partir d'un périphérique tel un iPhone.

### Bouton qui lance l'appel

Lors de l'appel de la fonction qui communiquer avec le service Web, il faudra prendre soin de le placer dans un `Task`, qui permet de lancer une tâche asynchrone.

Puisque cette fonction est déclarée avec `async`, l'exécution de la fonction doit utiliser `await`.

```swift title="SwiftUI"
Task {
  do {
    try await appelerService(items: ...)
  } catch {
    print(error.localizedDescription)
    ...   // mécanisme pour afficher un message à l'usager
  }
 }
```

### Démonstration

Et voici le code de la fonction qui communiquer avec le service Web.

```swift title="SwiftUI"
/**
 Appelle le service Web qui synchronise les données dans le nuage.
*/
func appelerService(items: [Item]) async throws {
  // Tente d'encoder les items en JSON
  let itemsJSON = try JSONEncoder().encode(items)

  // URL du service Web
  guard let url = URL(string: "http://127.0.0.1/monapi/synchro-items.php") else {
    // Arrivera ici si l'URL est invalide, par exemple s'il s'agit d'une chaîne vide ou qui contient des caractères accentués.
    throw URLError(.badURL)
  }

   // Initialisation de la requête
  var request = URLRequest(url: url)
  request.setValue("application/json", forHTTPHeaderField: "Content-Type")
  request.setValue("application/json", forHTTPHeaderField: "Accept")
  request.httpMethod = "POST"
  request.httpBody = itemsJSON

  // lance la requête HTTP
  let (data, response) = try await URLSession.shared.data(for: request)

  // lève une exception si le code d'état HTTP n'est pas 200
  guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
    throw URLError(.badServerResponse)
  }

  // décode la réponse JSON
  let reponseDecodee = try JSONDecoder().decode(ReponseDuService.self, from: data)
  // print(reponseDecodee)
  ...   // faire quelque chose avec la réponse
 }
```

## Consommer et déboguer un service Web - exemple avec service qui retourne une image

Il est très fréquent qu'une application mobile ait besoin de consommer un API (**Application Programming Interface**), aussi appelé **service Web**.

En effet, l'application mobile ne peut pas avoir directement accès à certains traitements côté serveur, par exemple enregistrer des données dans une base de données distante. Les API leur donnent accès à ce type de traitement.

De plus, comme pour toute application mobile, Web ou de bureau, il est intéressant de pouvoir accéder à des API qui fournissent des informations ou même des images sans qu'on ait à gérer les données ni à effectuer les traitements requis.

### Données échangées

Avant de vous lancer dans le projet, vous devez savoir quelles données sont attendues par l'API et quelles données sont retournées.

S'il s'agit de données complexes, elles seront généralement encodées au format JSON. Vous devrez alors créer un modèle [qui répond au protocole Encodable pour l'envoi ou au protocole Decodable pour la réception](conversion-json-codable-encodable-decodable.md#codable-pour-permettre-lencodage-et-le-decodage-json).

Vous pouvez également utiliser le protocole `Codable` qui regroupe les deux.

### Cat API

Je vous fais ici une démonstration en utilisant Cat API : <https://getcat.dev/>  

![Application démo pour async/await](images/application-mes-minous.webp){width=300}

Cet API fournit au hasard une image de chat à l'aide de la requête GET `https://api.getcat.dev/`.

#### Données retournées par Cat API

Pour connaître le format des données retournées par un API dont la une requête HTTP est de type GET, il suffit d'entrer son URL dans un navigateur.

Si la requête doit être de type POST, vous devrez plutôt utiliser un outil spécialisé pour tester les requêtes REST, par exemple [Postman](synchronisation-des-donnees-locales-dans-le-nuage.md#tester-un-service-web-api-manuellement-avec-postman), [Bruno](https://www.usebruno.com/) ou [curl](https://curl.se/).

Dans le cas de Cat API, l'appel est de type GET.

L'information retournée est au format :  
```json
{
  "url": "https://cdn.getcat.dev/cats/42.jpg"
}
``` 

Voici donc la structure requise pour stocker ces informations.

Remarquez qu'il n'est pas obligatoire que la structure reçoive toutes les informations retournées.

À l'inverse, toutes les informations de la structure doivent pouvoir être initialisées par la réponse. Dans le cas où l'une des informations n'est pas toujours retournée, elle doit pouvoir être initialisée à nil. C'est le cas ici pour le code qui n'a une valeur que lorsqu'une erreur est rencontrée.

Cette variable n'est jamais utilisée dans le code que je vous présente plus bas mais j'ai choisi de la placer dans ma structure au cas où je voudrais en tenir compte plus tard.

```swift title="Fichier Models/ReponseApi.swift"
/// Pour recevoir les informations en provenance de l'API Cat Api : https://api.getcat.dev/ (aucune clé requise)
struct ReponseApi: Decodable {
  var url: String
}
```

### Exemple d'application qui utilise Cat API

Passons maintenant à l'appel asynchrone de l'API.

Dans cet extrait de code, les couleurs réfèrent aux explications fournies plus bas.

```swift title="SwiftUI"
import SwiftUI

struct ContentView: View {
  @State private var reponseApi: ReponseApi? = nil
  @State private var messageErreur = ""

  var body: some View {
    NavigationStack {
      VStack {

        if messageErreur.isEmpty {

          Spacer()

          if reponseApi == nil {
            ProgressView()
          }
          else {
            AsyncImage(
              url: URL(string: reponseApi?.url ?? ""),
              content: { image in
                image
                  .resizable()
                  .scaledToFit()
                  .cornderRadius(12)
                  .padding()
              },
              placeholder: {
                ProgressView()
              }
            )
          }

          Spacer()

          // on veut un bouton seulement si une image a été affichée
          if let message = reponseApi?.url, !message.isEmpty {
            Button(action: {
              taskPourAppelerApi()
            }) {
              Text("Nouvelle image")
                .padding()
                .foregroundColor(Color.white)
                .background(Color.gray)
                .cornerRadius(15.0)
            }
            .padding()
          }
        }
        else {
          ContentUnavailableView {
            Label(messageErreur, systemImage: "wifi.slash")
          } actions: {
            Button("Réessayer") {
              taskPourAppelerApi()
            }
          }
        }
      } // fin VStack
      .navigationTitle("Les minous")
    } // fin NavigationStack
    .onAppear {
      // Image chargée au départ
      taskPourAppelerApi()
    }
  }

  /// Regroupe tout le code du bouton qui appelle l'API,
  /// incluant le Task et le do catch.
  func taskPourAppelerApi() {
    Task {
      do {
        reponseApi = nil   // si le nouvel appel ne fonctionne pas, l'ancienne image ne sera plus visible
        reponseApi = try await appelerApi()
        messageErreur = ""
      } catch {
        print(error.localizedDescription)
        messageErreur = "Impossible de retrouver l'image"
      }
    }
  }

  /**
   Appelle le service Web qui retourne l'URL d'une image de chat.

   - Returns : réponse du service Web
  */
  func appelerApi() async throws -> ReponseApi {

    let chaineURL = "https://api.getcat.dev/"

    guard let url = URL(string: chaineURL) else {
      // Arrivera ici si l'URL est invalide, par exemple s'il s'agit d'une chaîne vide ou qui contient des caractères accentués.
      throw URLError(.badURL)
    }

    // lance la requête HTTP
    let (data, response) = try await URLSession.shared.data(from: url)

    // retrouve le code d'état HTTP (cette structure permet au besoin de réagir différemment selon le code d'état)
    let etatHTTP = (response as? HTTPURLResponse)?.statusCode

    switch etatHTTP {
    case 200 :
      // décode la réponse JSON (sera rattrapé dans le catch si ne réussit pas)
      let reponseDecodee = try JSONDecoder().decode(ReponseApi.self, from: data)
      return reponseDecodee
    case 404 :
      print("Ressource inexistante")
      ... // au besoin, on peut effectuer un traitement propre à ce cas
      throw URLError(.fileDoesNotExist)
    case 500 :
      print("Erreur d'exécution")
      ... // au besoin, on peut effectuer un traitement propre à ce cas
      throw URLError(.badServerResponse)
    default :
      print("Code d'état HTTP : \(etatHTTP)")
      throw URLError(.badServerResponse)
    }
  }
}
```

### Quelques explications s'imposent!

#### async/await

Parlons d'abord de `async`/`await`.

Pour effectuer un appel asynchrone avec cette technique, il faut utiliser le mot-clé `async` lors de la déclaration de la fonction et le mot-clé `await` lors de son appel.

Remarquez que le mot-clé `await` apparaît également lors de l'appel de URLSession.shared.data(). C'est que cette fonction, qui fait partie de la bibliothèque Foundation, est également déclarée avec `async`.

#### Task et .task

La structure Task que l'on retrouve dans l'action du bouton permet de lancer une tâche asynchrone lorsque le bouton est pressé.

Notez que lors du chargement de la vue, il est souvent possible d'utiliser la méthode [.task](https://developer.apple.com/documentation/swiftui/view/task(name:priority:file:line:_:)) plutôt que `.onAppear` pour appeler une fonction asynchrone.

En effet, `.task{ ... }` est l'équivalent de `.onAppear { Task { ... } }`.

`.task` n'a pas été utilisé dans cet extrait de code puisque lors du chargement de la vue, on appelle une fonction qui, elle, se charge du `Task`.

#### Requête HTTP

La requête HTTP de cet exemple est de type GET. C'est pourquoi le paramètre passé à URLSession.shared.data() est un URL.

Si vous devez lancer une requête HTTP de type POST ou si vous avez des informations à fournir dans l'en-tête HTTP, [il faudra initialiser une variable de type URLRequest](consommer-un-service-web-avec-swiftui.md#consommer-un-service-web-de-type-get-ou-post) et la fournir en paramètre à `URLSession.shared.data()`.

Cette requête retourne deux informations :

- data : c'est le corps de la réponse HTTP. Cette variable contient les données retournées par le service Web.
- response : ce sont les métadonnées de la réponse. Elles permettent de retrouver, par exemple, le code d'état HTTP, les en‑têtes HTTP (headers), la taille du contenu, le type MIME.

#### Code d'état HTTP de l'API

Pour vérifier le code d'état HTTP retourné par l'API, il faut convertir la réponse au type HTTPURLResponse. Lopérateur [as?](https://docs.swift.org/swift-book/LanguageGuide/TypeCasting.html#ID341) permet de réaliser cette conversion. Il retournera la valeur `nil` si la conversion ne peut pas avoir lieu.

#### Décodage JSON

Finalement, l'information JSON retournée par l'API sera décodée afin de pouvoir être utilisée comme une variable du type requis.

### Tester l'appel à l'API

Voici quelques tests à réaliser afin de vous assurer que le code réagira correctement dans différentes situations.

- Modifiez l'URL pour un URL inexistant.
- Si vous utilisez un URL en ligne, modifiez-le pour qu'il débute par http://.
- Modifiez l'URL pour qu'il commence par un /.
- Si le service Web nécessite une clé d'API, ajoutez un X au début de cette clé.
- Modifiez le type de la propriété `status` dans votre modèle pour que ce soit un Int.
- Désactivez le Wi-Fi de votre Mac afin que le simulateur réagisse comme s'il n'avait pas de réseau.
- Lancez l'application avec le Wi-Fi activé (la première image sera générée) puis désactivez le Wi-Fi avant de cliquer sur le bouton de regénération.
- Si le service Web le permet, mettez en place les conditions pour qu'il ne retourne pas un code d'état HTTP 200.
- Finalement, faites un test dans lequel tout fonctionne correctement. Est-ce que le code fait ce qu'il doit faire?

### Techniques de débogage

Si l'appel de l'API ne fonctionne pas, c'est une bonne idée d'afficher dans la console lldb le code d'état HTTP afin de faciliter le débogage.

Avec la structure de code présentée plus haut, c'est relativement facile à faire.

Mais si vous avez une structure comme celle-ci :

```swift title="SwiftUI"
// Ce code fonctionne bien mais ne permet pas de connaître le code d'état HTTP en cas de problème
 guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
  throw URLError(.badServerResponse)
 }
```

Remplacez-la comme suit :

```swift title="SwiftUI"
guard let httpResponse = response as? HTTPURLResponse else {
  throw URLError(.badServerResponse)
 }

 if httpResponse.statusCode != 200 {
  print("État HTTP: \(httpResponse.statusCode)")
  print(String(data: data, encoding: .utf8)!)   // pour afficher le message du service Web, s'il y a lieu
  throw URLError(.badServerResponse)
 }
```

Si le décodage de la réponse ne fonctionne pas, vous pouvez essayer ceci pour vous aider à cerner le problème :

- Faire afficher dans la console lldb les données brutes avant de tenter le décodage.

  ```swift title="SwiftUI"
  print(String(data: data, encoding: .utf8)!)
  let reponseDecodee = ...
  ```
- Plutôt que de laisser le code lever une exception tout seul, entourer le décodage de do ... catch et faire afficher l'erreur dans la console lldb.  

  ```swift title="SwiftUI"
  do {
    let reponseDecodee = try JSONDecoder().decode(ReponseApi.self, from: data)
    return reponseDecodee
  } catch {
    print("Erreur JSON :", error)
    throw error
  }
  ```

## Consommer un service Web de type GET ou POST

Un service Web peut nécessiter une requête HTTP de type GET ou de type POST.

Dans tous les cas, l'URL du service Web doit être représenté par un objet de type URL.

```swift title="SwiftUI"
let chaineURL = "https://monapi.com"
guard let url = URL(string: chaineURL) else {
  throw URLError(.badURL)
}
```

### Appel de type GET

La requête HTTP de type GET est la plus simple à réaliser.

```swift title="SwiftUI"
let (data, response) = try await URLSession.shared.data(from: url)
// pour la suite, un exemple est donné sur la fiche « Consommer et déboguer un service Web - exemple avec service qui retourne une image ».
```

Notez que si le service Web nécessite des données en entrée, elles seront passées directement dans l'URL.

Selon la façon dont le service Web a été codé, l'URL peut contenir des paramètres dans son chemin.

```swift title="SwiftUI"
let chaineURL = "https://monapi.com/details/12
```

D'autres services sont codées pour que les données soient fournies en tant paramètres de requête.

```swift title="SwiftUI"
let chaineURL = "https://monapi.com?cle=valeur"
```

### Appel de type POST

Dans le cas d'un service Web qui travaille en POST, il faudra prévoir quelques étapes supplémentaires afin de fournir toutes les informations et configurations requises.

#### Encodage des données à envoyer au serveur

Certains services Web attendent des données en entrée.

La façon d'encoder les données dépendra du type d'encodage attendu par le service Web, qui doit être spécifié dans l'en-tête HTTP à l'aide de la configuration `Content-Type`.

##### application/json

Lorsque l'encodage attendu est en JSON, on pourra encoder les données comme suit :

```swift title="Swift"
let donneesJSON = try JSONEncoder().encode(["nom": "Annie", "age": "18"])
```

Rappel : avec Swift, un tableau associatif s'appelle [dictionnaire](https://developer.apple.com/documentation/swift/dictionary). Ses clés doivent toutes être du même type, généralement String.

Ses valeurs doivent également toutes être du même type. C'est pourquoi la valeur `18` est entourée de guillemets dans l'exemple précédent.

Pour transmettre cette chaîne JSON dans le corps du message :

```swift title="Swift"
request.httpBody = donneesJSON   // voir plus bas pour l'initialisation de request
```

##### text/plain

Dans le cas où l'encodage attendu est en texte, il est possible de fournir les informations sous forme de chaîne au format `nom=Annie&age=18`.

Cette chaîne pourra être générée à partir d'un dictionnaire comme suit :

```swift title="Swift"
// ligne empruntée, inspirée de https://stackoverflow.com/questions/26372198/convert-swift-dictionary-to-string
 let donneesTexte = tableauDonnees.map { $0.0 + "=" + $0.1 }.joined(separator: "&")
```

Pour transmettre cette chaîne dans le corps du message :

```swift title="Swift"
request.httpBody = donneesTexte.data(using: String.Encoding.utf8);
```

#### Configuration de la requête

La configuration de la requête est une étape importante. On pourra spécifier, par exemple :

- [httpMethod](https://developer.apple.com/documentation/foundation/urlrequest/2011415-httpmethod) : la méthode utilisée (POST, GET, PUT, PATCH, DELETE)
- les [informations d'en-tête HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) :
  - [Content-Type](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Content-Type) : type de données que le client (le programme que vous êtes en train d'écrire) envoie au serveur dans le corps de la requête HTTP (**body**), par exemple `"application/json"`, `"text/plain"`. Note : certains développeurs spécifient également l'encodage (ex : `"application/json; charset=utf-8"`) mais puisque l'encodage par défaut du JSON est UTF-8, il est inutile de le spécifier dans ce cas.
  - [Accept](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Accept) : type de données qui sont attendues par le client. Autrement dit, type de données que le serveur retourne dans sa réponse HTTP
  - [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) : informations qui permettent au service Web d'identifier d'où provient la requête HTTP. Il s'agit d'une chaîne qui peut contenir par exemple le nom de l'application qui lance la requête HTTP, sa version, les coordonnées de son auteur, etc.
  - [Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) : clé utilisée dans un mécanisme pour prouver qui est à l'origine de l'appel. Notez que certains services Web utilisent plutôt une clé d'API qui devra faire partie de l'URL ou du corps de la réponse
- [httpBody](https://developer.apple.com/documentation/foundation/urlrequest/2011390-httpbody) : les informations à fournir dans le corps de la requête. On y retrouvera notamment les données à envoyer au serveur. Notez que certains services Web pourraient attendre les données directement dans l'URL.

Au final, la configuration de la requête pourrait ressembler à ceci :

```swift title="SwiftUI"
var request = URLRequest(url: url)
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
request.setValue("application/json", forHTTPHeaderField: "Accept")
request.httpMethod = "POST"
request.httpBody = donneesJSON
```

#### Appel du service Web

Une fois les odnnées encodées et la requête HTTP configurée, il est possible d'effectuer l'appel.

```swift title="SwiftUI"
let (data, response) = try await URLSession.shared.data(for: request)
// pour la suite, un exemple est donné sur la fiche « Consommer un service Web pour synchroniser les données ».
```

## Les codes d'état HTTP

Lorsqu'un navigateur charge une page Web, la page peut être chargée avec succès ou retourner une erreur. Dans tous les cas, elle est accompagnée d'un code d'état HTTP.

Les codes rencontrés le plus fréquemment sont :

- 200 (succès)
- 404 (page non trouvée)
- 500 (erreur d'exécution dans l'application)

### Catégories pour les codes d'état HTTP

Selon le [Internet Engineering Task Force](https://www.ietf.org/) (IETF), les codes d'état HTTP sont regroupés en [différentes catégories](https://www.rfc-editor.org/rfc/rfc9110#name-status-codes).

Le premier chiffre du code d'état représente sa catégorie.

- 1xx (Information)
- 2xx (Succès)
- 3xx (Redirection)
- 4xx (Erreur côté client)
- 5xx (Erreur côté serveur)

### Liste des codes d'état HTTP

Voici d'autres codes que vous pourriez rencontrer. La liste complètes est disponible ici : [https://www.rfc-editor.org/rfc/rfc9110](https://www.rfc-editor.org/rfc/rfc9110#name-status-code-registration).

Certains sites peuvent utiliser des codes qui ne font pas partie de la liste de l'IEFT. Ces codes non conformes sont indiqués par un astérisque.

| Code | Message | Signification |
| --- | --- | --- |
| 101 | Switching Protocols | Changement de protocole, par exemple pour une communication via WebSockets |
| 200 | OK | Requête réussie |
| 203 | Non-Authoritative Information | Information retournée, mais générée par une source non certifiée |
| 301 | Moved Permanently | Site déménagé de façon permanente |
| 302 | Moved Temporarily | Site déménagé de façon temporaire |
| 304 | Not Modified | Rien de changé, version en cache utilisée |
| 400 | Bad Request | Un problème de syntaxe empêche le serveur de comprendre la requête |
| 401 | Unauthorized | Utilisateur non authentifié |
| 403 | Forbidden | Accès refusé car l'usager ne détient pas les droits requis pour effectuer l'opération.  Sous Laravel, ceci se produit si le nom de domaine ne pointe pas sur le dossier public.  Peut également survenir lorsque le serveur détecte une tentative d'attaque. |
| 404 | Not Found | Page ou ressource non trouvée |
| 405 | Method Not Allowed | Méthode non autorisée, possiblement parce qu'on essaie d'atteindre une ressource par GET alors que seul POST est autorisé ou vice-versa |
| 408 | Request Timeout | Délai dépassé par la requête |
| 419* | Unknown status | Statut inconnu.  Pourrait être causé, par exemple, par un problème avec la protection anti-CSRF ou, lors d'un appel AJAX, par une mauvaise configuration Content-Type. |
| 422 | Unprocessable entity | Entité fournie avec la requête non compréhensible, possiblement à cause d'une erreur de validation |
| 429* | Too Many Requests | Trop de requêtes, possiblement à cause d'un robot malveillant qui tente une attaque |
| 500 | Internal Server Error | Erreur d'exécution dans l'application |
| 502 | Bad Gateway ou Proxy Error | Le serveur a reçu une réponse non valide d'un autre serveur alors qu'il agissait en tant que passerelle ou proxy.  Ceci peut survenir, par exemple, quand une requête fetch attend du JSON et qu'elle reçoit du HTML. |
| 503 | Service Unavailable | Service non accessible de façon temporaire, comme par exemple lors de la maintenance du site Web |

* Code qui ne fait pas partie de la liste de l'[IEFT](https://www.ietf.org/).

### Quel est le code d'état de la page actuellement affichée ?

Il est possible de connaître le code d'état HTTP d'une page Web et des différents fichiers qu'elle utilise comme suit :

- Affichez la page Web dans Google Chrome.
- Faites un clic droit sur la page / **Inspecter l'élément** ou appuyez sur <kbd>F12</kbd> (Outils de développement).
- Cliquez sur **Network**.
- Rafraîchissez la page. Dans la colonne **Status**, vous verrez les codes d'état des différents fichiers chargés par la page.

  ![Codes d'état HTTP dans Chrome](images/Chrome-AfficherCodeEtatHTTP.png)

### Pour plus d'information

« HTTP response status codes ». MDN. <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>

« RFC 9110 HTTP Semantics - Status Code Registration ». IETF. <https://www.rfc-editor.org/rfc/rfc9110#name-status-code-registration>

« Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content ». Internet Engineering Task Force (IETF) . <https://datatracker.ietf.org/doc/html/rfc7231#page-49>

« Liste des codes HTTP ». Wikipedia. <http://fr.wikipedia.org/wiki/Liste_des_codes_HTTP>

## Vérifier le code d'état HTTP dans Chrome

Lorsqu'on ouvre une page Web dans Google Chrome, il est possible de vérifier le [code d'état HTTP](consommer-un-service-web-avec-swiftui.md#les-codes-detat-http) retourné pour chacune des ressources chargée par la page.

Il en va de même lorsqu'on fait appel à un service Web.

Pour voir le code d'état HTTP dans Google Chrome :

- Faites afficher les outils de développement de Chrome (<kbd>F12</kbd> sous Windows ou <kbd>⌘ Cmd</kbd>+<kbd>⌥ Option</kbd>+<kbd>I</kbd> sous Mac).
- Ouvrez l'onglet **Réseau** (ou **Network**).
- Entrez l'URL désiré ou rafraîchissez l'écran s'il était déjà chargé.
- Le code d'état de chaque ressource apparaît dans la zone inférieure.

![Code d'état HTTP dans Chrome](images/Web-RetrouverCodeEtatHTTP-Site.png)

### Service Web pour tester les codes d'état HTTP

Je vous fais une seconde démonstration ici avec un service Web de type GET dont le but est justement de tester les réactions d'une application selon le code d'état HTTP retourné par ce service.

Le code de ce service Web est tout simple :

```python title="python"
/**
 * Pour tester les codes d'état HTTP d'un service Web ainsi que les valeurs retournées.
 * @author Étienne Rivard
 * Utilisation dans le navigateur :
 * https://test.profinfo.ca/ -> donne erreur 404
 * https://test.profinfo.ca/?etat=200 -> donne une erreur 200
 * https://test.profinfo.ca/?etat=500 -> donne une erreur 500
 */
from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.ensure_ascii = False  # keep accents readable in JSON ("Réussi!")


@app.route("/")
def etat():
    valeur = request.args.get("etat")

    # No "etat" in the URL -> 404
    if valeur is None or valeur == "":
        return jsonify(code=3, message="Information manquante"), 404

    # "etat" must be a valid HTTP status code to be used as the response code
    try:
        http_response_code = int(valeur)
    except ValueError:
        http_response_code = None
    if http_response_code is None or not 100 <= http_response_code <= 599:
        return jsonify(code=2, message="Erreur non traitée"), 400

    if http_response_code == 200:
        return jsonify(code=1, message="Réussi!"), http_response_code

    return jsonify(code=2, message="Erreur non traitée"), http_response_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

J'ai mis ce service Web en ligne à l'adresse  `https://test.profinfo.ca/ `.

Pour que le service Web retourne le code d'état HTTP 403, il faut lui passer cet état en paramètre dans l'URL : `https://test.profinfo.ca/?etat=403`.

![Code d'état HTTP dans Chrome](images/Web-RetrouverCodeEtatHTTP.png)

## L'authentification auprès du service Web

Lorsqu'un service Web est en ligne, il faut s'assurer que les seuls usagers ou applications distantes qui peuvent y accéder sont ceux qui en ont le droit.

Dans sa forme la plus simple, l'authentification consistera à un code d'usager combiné à un mot de passe qui seront transmis au service Web afin qu'il confirme l'identité et les droits qui y sont rattachés.

Si plusieurs aller-retours doivent être faits entre l'application distante et le service Web, on pourra implanter un mécanisme de [d'authentification avec jeton](consommer-un-service-web-avec-swiftui.md#bearer-authentication-et-json-web-token).

## Bearer authentication et JSON Web Token

Pour qu'une application distante soit autorisée à utiliser un service Web, il est possible de travailler avec un mécanisme de jeton.

On appellera ce mécanisme **Bearer authentication** (littéralement authentification du porteur) ou **Token authentication**.

En gros, le fonctionnement va comme suit :

1. Pendant une session de travail, la première fois que l'application distante a besoin du service Web, elle lui fournit des informations d'authentification (code d'usager - mot de passe).
2. Lorsqu'il détecte qu'il a reçu un code d'usager et un mot de passe, le service Web vérifie ces informations et, si elles sont valides, il retourne un jeton.
   1. Le jeton peut être une simple chaîne générée du côté serveur, par exemple avec random_bytes().
   2. Pour plus de sécurité, on peut utiliser un jeton Web JSON (**JSON Web Token** ou JWT). Il s'agit ici encore d'une chaîne générée par le serveur mais cette chaîne contient des informations qui sont cryptées. La chaîne est en fait composée de trois parties : l'en-tête (**header**), les données (charge utile, **payload**) et la signature (**signature**).
3. Lors des appels suivants, l'application fournit le jeton dans son entête HTTP. Le service Web s'assure que le jeton est valide et si oui, il effectue le travail demandé.

Je vous explique ici comment générer un jeton JWT.

### Génération de la clé secrète

Le service Web doit posséder une clé secrète qui sera utilisée pour créer le jeton JWT.

Cette clé secrète, qui ne doit être connue que par le service Web, sera utilisée plus précisément pour hacher la signature du jeton JWT.

Pour générer une clé secrète :

```php title="PHP"
$secret = bin2hex(random_bytes(32));
echo $secret;
```

Vous pouvez maintenant mettre ces lignes en commentaire (ou les supprimer) et ajouter la clé secrète dans votre fichier de configurations.

```php title="PHP"
$secret = 'a930902390832e7090c889d7fe1eea6a5d89e186631a08540ed017a554fe4774';
```

### Génération du jeton par le service Web

En PHP, le jeton peut être généré à l'aide d'une bibliothèque telle que [ReallySimpleJWT](https://github.com/RobDWaller/ReallySimpleJWT).

Il est également possible de générer le jeton à l'aide de cet extrait de code inspiré de l'article « Create Your JWTs From Scratch » disponible ici : <https://dzone.com/articles/create-your-jwts-from-scratch>.

```php title="PHP"
/**
 * Effectue l'encodage en base64 d'une chaîne et la rend propre à être utilisée dans un URL.
 * Source : https://dzone.com/articles/create-your-jwts-from-scratch
 *
 * @param String $text Texte à encoder.
 *
 * @return string Texte encodé.
 *
 */
// PHP has no function, so let's define one that
// does some magic by replacing + with -, / with _ and = with ''.
// This way we can pass the string within URLs without
// any URL encoding.
function base64UrlEncode($text) {
    return str_replace(
        ['+', '/', '='],
        ['-', '_', ''],
        base64_encode($text)
    );
}

/**
 * Génère un jeton JWT.
 * Inspiré de https://dzone.com/articles/create-your-jwts-from-scratch
 *
 * @param String $secret Chaîne secrète.
 * @param Int $login Code d'authentification de l'usager.
 *
 * @return string Jeton JWT.
 *
 */
function genererJWT($secret, $login) {
    $header = json_encode([
        'typ' => 'JWT',
        'alg' => 'HS256'
    ]);

    $payload = json_encode([
        'login' => $login,
        'exp' => time() + 3600
    ]);

    $base64UrlHeader = base64UrlEncode($header);
    $base64UrlPayload = base64UrlEncode($payload);
    $signature = hash_hmac('sha256', $base64UrlHeader . "." . $base64UrlPayload, $secret, true);
    $base64UrlSignature = base64UrlEncode($signature);

    $jwt = $base64UrlHeader . "." . $base64UrlPayload . "." . $base64UrlSignature;

    return $jwt;
}
```

Un echo permet de prendre connaissance de la valeur du jeton.

```php title="PHP"
$jeton = genererJWT($secret, "toto");
echo $jeton;
```

Vous obtiendrez une chaîne au format eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRvdG8iLCJleHAiOjE3MTA3NzM1Mzd9.VWfTYzfCz39_brOUK7IQtfG407mFIoky6jgm0EKZ4W4

Certaines parties de cette chaîne peuvent être  décryptées : l'entête et la charge utile. Seule la signature est hachée donc indécryptable.

À preuve, vous pouvez décrypter le jeton avec ce petit utilitaire : [https://www.jsonwebtoken.io](https://www.jsonwebtoken.io/)

![Décoder un JWT](images/DecodeJWT.png)

### Vérification du jeton

Quand le service Web reçoit un jeton JWT, il peut utiliser cette fonction pour valider le jeton.

```php title="PHP"
/**
 * Vérifie si un jeton JWT est valide.
 * Inspiré de https://dzone.com/articles/create-your-jwts-from-scratch
 *
 * @param String $secret Chaîne secrète.
 * @param String $jwt Jeton à valider.
 *
 * @return Bool True si le jeton est valide.
 *
 */
function validerJWT($secret, $jwt) {
    $tokenParts = explode('.', $jwt);
    $header = base64_decode($tokenParts[0]);
    $payload = base64_decode($tokenParts[1]);
    $signatureProvided = $tokenParts[2];

    // check the expiration time - note this will cause an error if there is no 'exp' claim in the token
    $now = time();
    $tokenExpired = ($now - json_decode($payload)->exp) > 0;

    // build a signature based on the header and payload using the secret
    $base64UrlHeader = base64UrlEncode($header);
    $base64UrlPayload = base64UrlEncode($payload);
    $signature = hash_hmac('sha256', $base64UrlHeader . "." . $base64UrlPayload, $secret, true);
    $base64UrlSignature = base64UrlEncode($signature);

    // verify it matches the signature provided in the token
    $signatureValid = ($base64UrlSignature === $signatureProvided);

    return !$tokenExpired && $signatureValid;
}
```

## Faire appel à un URL non sécurisé

Normalement, lorsqu'une application SwiftUI fait appel à un service Web en ligne, l'URL est sécurisé, c'est-à-dire qu'il débute par `https://`.

Si vous désirez travailler avec service Web local pendant la phase de développpement, l'URL pourrait ne pas être sécurisé. Il pourrait, par exemple, être au format `http://127.0.0.1:5000/monserviceweb`.

Si vous utilisez un URL non sécurisé avec la fonction `URLSession()`, vous obtiendrez, selon la version de Swift, un message du genre :

- « An SSL error has occurred and a secure connection to the server cannot be made. »
- ou « The resource could not be loaded because the App Transport Security policy requires the use of a secure connection. »
- ou encore « App Transport Security has blocked a cleartext HTTP connection to ... since it is insecure. Use HTTPS instead or add this domain to Exception Domains in your Info.plist. ».

```swift title="SwiftUI"
guard let url = URL(string: "http://127.0.0.1:5000") else {
  throw URLError(.badURL)
 }

var request = URLRequest(url: url)
...

let (data, response) = try await URLSession.shared.data(for: request)   // cette ligne lèvera une exception
```

### Permettre un URL non sécurisé spécifique

Il est possible d'informer SwiftUI que vous désirez effectuer une requête non sécurisée avec un URL précis. Tous les autres URL non sécurisés seront bloqués.

Ceci est réalisé en ajoutant une entrée dans [Info.plist](info-plist.md#ajouter-une-paire-cle-valeur-dans-infoplist).

- Dans le navigateur de projet de Xcode (s'il n'est pas visible, cliquez sur l'icône de chemise ![Icône chemise, filière](../10-introduction-a-swift/images/Xcode-IconeChemise.png) dans la zone de gauche), cliquez sur le nom du projet.
- Rendez-vous dans l'onglet **Info**.
- Dans la section **Custum iOS Target Properties**, pointez la souris vis-à-vis n'importe quelle clé puis cliquez sur +.
- Entrez le nom de clé `NSAppTransportSecurity` (App Transport Security Settings). Xcode indiquera qu'il s'agit d'un dictionnaire.
- Il faut maintenant préciser quel URL peut être utilisé même s'il n'est pas sécurisé. Commencez par cliquer sur le chevron (>) vis-à-vis la clé comme si vous désiriez afficher ses enfants (il n'y en a présentement aucun).
- Une fois la clé « ouverte », cliquez sur le + à sa droite pour ajouter un enfant.  

  ![App Transport Security Settings / Add Row](images/Xcode-InfoPlist-NSAppTransportSecurity.png)
- Entrez la clé `NSExceptionDomains` ou sélectionnez **Exception Domains**. Xcode indique qu'il s'agit d'un dictionnaire.
- Ouvrez cette nouvelle clé puis cliquez sur le + à sa droite.
- Entrez votre **nom de domaine** sans le http:// et sans nom de fichier (ex : mondomaine.com et non http://mondomaine.com/mapage.php).
- Ici, c'est à vous de spécifier qu'il s'agit d'un dictionnaire.
- Ouvrez encore une fois la nouvelle clé puis cliquez sur le + à sa droite.
- Entrez la clé `NSExceptionAllowsInsecureHTTPLoads`.
- Vous devez spécifier que son type est Boolean.
- Donnez-lui la valeur YES.

  ![clé NSAppTransportSecurity et ses enfants](images/Xcode-InfoPlist-NSAppTransportSecurity-2.png)
