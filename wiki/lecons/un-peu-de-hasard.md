# Un peu de hasard

## random()

La méthode [random()](https://developer.apple.com/documentation/swift/int/2995648-random) permet de générer un nombre au hasard.

```swift title="Swift"
nombre = Int.random(in: 1..<50)
```

[Deux opérateurs sont disponibles pour définir l'étendue](../complements/le-langage-swift-reference.md#les-operateurs-dintervalle) :

- `a...b` (opérateur d'intervalle fermé ou, en anglais, **closed range operator**) : les trois points indiquent que les valeurs a et b sont incluses
- `a..<b` (opérateur d'intervalle semi-ouvert ou, en anglais, **half-open range operator**) : les deux points suivis du signe « plus petit que » indiquent que a est inclus mais b est exclu

Si vous avez besoin d'un nombre qui n'est pas un entier, il est possible d'utiliser le type approprié devant l'appel de `random()`.

```swift title="Swift"
montant = Double.random(in: 1...50)
positionX = CGFloat.random(in: 1...50)
```

## randomElement()

Lorsqu'on a en main une collection de données, par exemple un tableau, il est possible de tirer une de ses données au hasard à l'aide de [randomElement()](https://developer.apple.com/documentation/swift/array/2994747-randomelement).

Mais cette fonction a des particularités qu'il faut comprendre pour bien l'utiliser.

Les précautions qui suivent sont nécessaires puisqu'une collection pourrait avoir été initialisée par programmation, par exemple à partir d'informations lues au clavier ou à partir de la base de données.

Le problème, c'est que si la collection est vide, `randomElement()` retournera nil. Donc, si on a un tableau de String, `randomElement()` retournera une variable de type String?, c'est-à-dire un String ou nil.

Si on ne tient pas compte de ce fait et qu'on écrit :

```swift title="Swift"
var info = infos.randomElement()
```

On obtiendra le message `Value of optional type 'String?' must be unwrapped to a value of type 'String'`{ .erreur }.

### Collection codée en dur

Lorsque la collection est codée en dur, donc qu'on est certains qu'elle ne sera jamais vide, on peut faire suivre l'appel de la fonction par un point d'exclamation.

Cet opérateur est utilisé pour ce qu'on appelle un **déballage forcé** (**Forced Unwrapping**).

Il signifie qu'on garantit que la valeur ne sera jamais nil. Si on utilise cet opérateur à un endroit non sécuritaire, le programme pourrait planter.

```swift title="Swift"
var info = infos.randomElement()!
```

### Collection générée dynamiquement

Lorsque la collection est créée dynamiquement, il est possible de faire précéder l'appel par un if.

```swift title="Swift"
if let info = infos.randomElement() {
    ...
 }
```

ou encore faire appel à l'[opérateur de fusion nil](https://docs.swift.org/swift-book/LanguageGuide/BasicOperators.html#:~:text=Nil-Coalescing%20Operator) (**Nil-Coalescing Operator**) pour spécifier la valeur à utiliser si la variable qui précède l'opérateur est à nil.

```swift title="Swift"
var info = infos.randomElement() ?? ""
```
