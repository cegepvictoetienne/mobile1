# CHHapticEngine

Alors que la classe [UINotificationFeedbackGenerator()](la-vibration.md) travaille avec des vibrations standardisées, la classe [CHHapticEngine](https://developer.apple.com/documentation/corehaptics/chhapticengine) peut émettre des vibrations qui correspondent à un patron que vous aurez vous-même créé. Il permet même de faire jouer un son pendant la vibration.

En passant, le terme **haptic** se traduit par **haptique**, c'est-à-dire ce qui concerne le sens du toucher.

Notez que si vous désirez émettre une vibration pour signaler un succès, un avertissement ou une erreur, vous devez plutôt utiliser [SensoryFeedback](la-vibration.md) puisqu'il s'agit de vibrations standardisées.

Voici les étapes à réaliser pour préparer le moteur de vibrations avec `CHHapticEngine`.

- Importez la bibliothèque `CoreHaptics`.

  ```swift title="SwiftUI"
  import CoreHaptics
  ```
- Déclarez une variable de type [CHHapticEngine](https://developer.apple.com/documentation/corehaptics/chhapticengine) qui peut être nulle. Dans cet exemple, je la déclare directement dans le ContentView alors il faut que ce soit une variable d'état pour qu'elle soit modifiable.  

  ```swift title="SwiftUI"
  @State private var engine: CHHapticEngine?
  ```
- Dans le `.onAppear()` du ContentView OU dans le constructeur de la classe que vous écrivez, vérifiez si l'appareil mobile supporte les vibrations. Si oui, instanciez l'objet et démarrez le moteur de vibrations.

  ```swift title="SwiftUI"
  guard CHHapticEngine.capabilitiesForHardware().supportsHaptics else { return }

   do {
    engine = try CHHapticEngine()
    try engine?.start()
   } catch {
    print("Le moteur de vibrations ne peut pas être démarré: \(error.localizedDescription)")
   }
  ```

## Faire jouer une vibration

Une fois le moteur démarré, il est possible de faire jouer une vibration.

C'est une bonne pratique de placer dans une fonction le code pour jouer la vibration.

La vibration sera définie à l'aide d'un événement qui définit si l'impulsion est simple (**transcient**) ou continue (**continuous**).

Pour chaque impulsion, il est possible de définir son intensité (**intensity**) et son acuité (**sharpness**).

```swift title="SwiftUI"
func jouerVibrationSimple() {
  // vérifier à nouveau si l'appareil mobile supporte les vibrations puisque la fonction pourrait être appelée même si le moteur de vibration n'est pas démarré
  guard CHHapticEngine.capabilitiesForHardware().supportsHaptics else { return }

  // code emprunté. Source : https://www.hackingwithswift.com/example-code/core-haptics/how-to-play-custom-vibrations-using-core-haptics
  let intensity = CHHapticEventParameter(parameterID: .hapticIntensity, value: 1)
  let sharpness = CHHapticEventParameter(parameterID: .hapticSharpness, value: 1)
  let event = CHHapticEvent(eventType: .hapticTransient, parameters: [intensity, sharpness], relativeTime: 0)

  do {
    let pattern = try CHHapticPattern(events: [event], parameters: [])
    let player = try engine?.makePlayer(with: pattern)
    try player?.start(atTime: 0)
  } catch {
    print("Impossible de faire jouer le patron: \(error.localizedDescription).")
  }
  // fin du code emprunté
}
```

## Patron de vibration codé dans un fichier AHAP

Il est possible de définir le patron de la vibration dans un [fichier AHAP](https://developer.apple.com/documentation/corehaptics/representing_haptic_patterns_in_ahap_files) (**Apple Haptic Audio Pattern**). Ce type de fichier utilise la syntaxe JSON.

Un peu comme pour une base de données SQLite, le fichier AHAP sera [ajouté dans le paquet de l'application](les-fichiers-du-paquet-de-l-application.md#ajouter-un-fichier-dans-le-paquet-de-lapplication).

Voici un exemple de fichier AHAP qui fait une seule petite vibration. Il est tiré du site <https://exyte.com/blog/creating-haptic-feedback-with-core-haptics>.

Vous y retrouverez les mêmes concepts (impulsion **transcient** ou **continous** et pour chacune, **intensity** et **sharpness**) que lorsque le patron est défini par programmation.

```text title="Fichier AHAP"
{
  "Version": 1.0,
  "Pattern": [
    {
      "Event": {
        "Time": 0.0,
        "EventType": "HapticTransient",
        "EventParameters": [
          {
            "ParameterID": "HapticIntensity",
            "ParameterValue": 1.0
          },
          {
            "ParameterID": "HapticSharpness",
            "ParameterValue": 0.6
          }
        ]
      }
    }
  ]
}
```

Voici un fichier un peu plus complexe que j'ai créé à l'aide de l'application Web [Captain AHAP](https://ahap.fancypixel.it/).

```text title="Fichier AHAP"
{
  "Version": 1,
  "Pattern": [
    {
      "Event": {
        "Time": 0.0,
        "EventType": "HapticTransient",
        "EventParameters": [
          {
            "ParameterID": "HapticIntensity",
            "ParameterValue": 1.0
          },
          {
            "ParameterID": "HapticSharpness",
            "ParameterValue": 0.2
          }
        ]
      }
    },
    {
      "Event": {
        "Time": 0.5,
        "EventType": "HapticContinuous",
        "EventDuration": 0.2,
        "EventParameters": [
          {
            "ParameterID": "HapticIntensity",
            "ParameterValue": 1.0
          },
          {
            "ParameterID": "HapticSharpness",
            "ParameterValue": 1.0
          }
        ]
      }
    }
  ]
}
```

Le chemin du fichier sera retrouvé par programmation juste avant ou après avoir démarré le moteur de vibration.

```swift title="SwiftUI"
// Retrouver le chemin du fichier AHAP dans le paquet
if let url = Bundle.main.url(forResource: "monFichier", withExtension: "ahap") {
  // on conserve l'URL dans une variable qui a une plus grande portée afin qu'elle soit visible dans la fonction qui fera jouer la vibration
  urlAhap = url
}
else {
  print("Impossible de charger monFichier.ahap.")
  return
}
```

Pour faire jouer la vibration, le code ressemblera à ceci :

```swift title="SwiftUI"
func jouerVibrationFichierAhap() {
  // vérifier à nouveau si l'appareil mobile supporte les vibrations puisque la fonction pourrait être appelée même si le moteur de vibration n'est pas démarré
  guard CHHapticEngine.capabilitiesForHardware().supportsHaptics else { return }

  do {
    // redémarrer le moteur au cas où il aurait été inactif (idle)
    try engine?.start()

    // faire jouer le patron
    try engine?.playPattern(from: urlAhap)
  } catch {
    print("Impossible de faire jouer le patron: \(error.localizedDescription).")
  }
}
```

## Fichier AHAP qui fait jouer un son

En plus de générer des vibrations, un fichier AHAP peut faire jouer un son ou même de la musique, par exemple à partir d'un fichier .wav.

Le fichier .wav peut démarrer au moment désiré pendant le patron de vibration. Il est possible qu'une vibration et le son jouent en même temps.

Ce fichier devra [être ajouté dans le paquet de l'application](les-fichiers-du-paquet-de-l-application.md#ajouter-un-fichier-dans-le-paquet-de-lapplication) au même titre que le fichier AHAP.

Voici un exemple de fichier AHAP qui charge un fichier .wav.

```text title="Fichier AHAP"
{
  "Version": 1,
  "Pattern": [
    {
      "Event": {
        "Time": 0.0,
        "EventType": "AudioCustom",
         "EventWaveformPath": "monSon.wav",
         "EventParameters": [
           {
             "ParameterID": "AudioVolume",
             "ParameterValue": 0.75
           }
         ]
      }
    },
    {
      "Event": {
         "Time": 0.00,
         "EventType": "HapticContinuous",
         "EventDuration": 0.25,
         "EventParameters": [
           {
             "ParameterID": "HapticIntensity",
             "ParameterValue": 0.4
           },
           {
             "ParameterID": "HapticSharpness",
             "ParameterValue": 0.4
           }
         ]
      }
    }
  ]
}
```

Pour faire jouer le son, il faut apporter un ajout au code qui démarre le moteur de vibration.

```swift title="SwiftUI"
guard CHHapticEngine.capabilitiesForHardware().supportsHaptics else { return }

 do {
   // pour permettre de jouer les sons inclus dans le fichier AHAP
  let audioSession = AVAudioSession.sharedInstance()

  engine = try CHHapticEngine(audioSession: audioSession)
  try engine?.start()

  // Retrouver le chemin du fichier AHAP dans le paquet
  if let url = Bundle.main.url(forResource: "monFichier", withExtension: "ahap") {
    // on conserve l'URL dans une variable qui a une plus grande portée afin qu'elle soit visible dans la fonction qui fera jouer la vibration
    urlAhapSimple = url
  }
  else {
    print("Impossible de charger monFichier.ahap.")
   return
  }
 } catch {
  print("Le moteur de vibrations ne peut pas être démarré: \(error.localizedDescription)")
 }
```

Il n'y a rien de plus à faire. Le fichier de son sera chargé automatiquement lorsque le patron du fichier AHAP sera joué.

## Pour plus d'information

« CHHapticEngine ». Apple. <https://developer.apple.com/documentation/corehaptics/chhapticengine>

« Preparing Your App to Play Haptics ». Apple. <https://developer.apple.com/documentation/corehaptics/preparing_your_app_to_play_haptics>

« How to play custom vibrations using Core Haptics ». Hacking with Swift. <https://www.hackingwithswift.com/example-code/core-haptics/how-to-play-custom-vibrations-using-core-haptics>

« Playing a Custom Haptic Pattern from a File ». Apple. <https://developer.apple.com/documentation/corehaptics/playing_a_custom_haptic_pattern_from_a_file>

« Representing Haptic Patterns in AHAP Files ». Apple. <https://developer.apple.com/documentation/corehaptics/representing_haptic_patterns_in_ahap_files>

« Practice audio haptic design ». Apple. <https://developer.apple.com/videos/play/wwdc2021/10278/>

« How to add CoreHaptics to your iOS app ». Medium. <https://medium.com/bilue/how-to-add-corehaptics-to-your-ios-app-bbc408860322>

«&nbspCaptain AHAP ». Fancy Pixel. <https://ahap.fancypixel.it/>
