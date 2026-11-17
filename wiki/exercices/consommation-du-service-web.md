# Exercice 13 : Consommation du service Web de synchronisation

Maintenant que vous avez en main un [service Web fonctionnel](service-web-de-synchronisation.md), vous devez le consommer dans votre application SwiftUI.

1. Ajoutez un bouton à votre application pour lancer la synchronisation. Un clic sur ce bouton encodera vos objets au format JSON puis effectuera l'appel du service Web.
2. L'usager doit être correctement informé du succès ou non de la synchronisation. Note : un `print()` n'est pas un message à l'usager puisqu'il n'apparaît que dans Xcode.
3. En cas de problème, utilisez un `ContentUnavailableView` pour informer l'usager.
