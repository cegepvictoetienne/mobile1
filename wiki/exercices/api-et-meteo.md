# Exercice 14 : API et météo

Dans cet exercice, vous serez appelé à travailler dans différents projets Xcode.

1. Créez une application pour afficher une photo de chat à partir d'un API. Voici quelques consignes en vrac :
    1. Utilisez le code fourni dans les [notes de cours](../lecons/consommer-un-service-web-avec-swiftui.md).
    2. Votre but : afin de mieux comprendre la gestion des erreurs, mettez en place les conditions pour que les différentes exceptions soient levées.
    3. Vous devez y arriver sans modifier la logique du code. Vous pouvez, par exemple, modifier l'URL, modifier le modèle de la réponse, etc. Quelques exemples de tests sont fournis dans les notes de cours.
    4. Ne passez pas plus de 10 minutes à essayer de faire lever les différentes exceptions.
    5. Pour tester comment l'application réagit si elle fait appel à un service Web qui retourne différents codes d'état HTTP, vous pouvez faire un test avec l'API `https://test.profinfo.ca/?etat=403`. Il retournera le code d'état passé dans l'URL ou 404 si le code est manquant. À vous de trouver le format des informations retournées.
2. Lors de la création de l'interface initiale de votre application sur les objets connectés, vous aviez prévu une icône qui donne accès à la météo. Vous devez maintenant coder cette fonctionnalité.
    1. Prenez le temps de centraliser les configurations de votre application, par exemple les coordonnées GPS qui seront utilisées par l'API Météo.
    2. Assurez-vous que la [clé d'API est stockée de façon sécurisée](../lecons/configurations-et-cles-d-api.md) (phase de développement seulement).
    3. Au départ, un clic sur l'icône Météo affichera une vue qui présente la température maximale d'aujourd'hui en degrés Celsius pour Victoriaville. Dans un premier temps, codez l'interface en dur. Vous devez faire afficher une image de votre choix et une température.
    4. Faites maintenant appel au service Web de OpenWeatherMap pour obtenir l'icône météo et la température maximale pour aujourd'hui à Victoriaville. Vous pouvez coder en dur la latitude et la longitude que le service Web doit utiliser.
    5. À l'aide du débogueur, vérifiez quel code d'état HTTP est retourné par l'API si vous tentez d'accéder à des informations réservées aux abonnements payants, par exemple les [prévisions pour 16 jours](https://openweathermap.org/forecast16).
    6. **OPTIONNEL** : lorsqu'on fait glisser la vue vers la gauche, on obtient la température maximale pour demain. Un glissement supplémentaire affichera la température maximale pour le jour suivant. Important : la date doit clairement apparaître pour chaque prévision mais l'heure ne doit pas être affichée. Puisque la version gratuite d'OpenWeatherMap donne la météo aux 3 heures, vous pouvez simplement prendre une des valeurs fournies à chaque jour, par exemple la météo à midi.
    7. **OPTIONNEL** : affichez une météo plus juste en calculant la vraie température maximale pour chaque jour. À vous de voir comment déterminer l'icône à afficher.
    8. **OPTIONNEL** : utilisez les capteurs du téléphone pour obtenir la latitude et la longitude afin d'afficher la météo qui correspond exactement à l'endroit où se trouve le téléphone.
    9. **OPTIONNEL** : ajoutez une option pour permettre l'affichage en Celsius ou en Fahrenheit.
    10. Remettez un zip de votre projet sur la plateforme électronique du cours.
