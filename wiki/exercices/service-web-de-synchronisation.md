# Exercice 12 : Service Web de synchronisation

Dans cet exercice, vous devez tester, ajuster et retester le service Web de synchronisation fourni dans les [notes de cours](../lecons/synchronisation-des-donnees-locales-dans-le-nuage.md).

Vous pouvez installer le service Web localement sur votre MacBook à l'aide de [Docker](../complements/docker-services.md) ou encore le mettre en ligne chez un hébergeur. Notez cependant que si le service Web est local, il pourra fonctionner avec le simulateur mais pas avec le iPhone.

Afin de simplifier le tout, vous n'avez pas besoin de coder l'authentification auprès du service Web.

Voici les étapes à réaliser :

1. Commencez par tester le code du service Web fourni dans les notes de cours à l'aide d'un [testeur de requêtes REST](../lecons/synchronisation-des-donnees-locales-dans-le-nuage.md#tester-un-service-web-api-manuellement-avec-postman) comme Postman ou [Bruno](https://www.usebruno.com/). Vous devrez créer une table `clients` dans une base de données MySQL.
2. Ajustez le service Web pour que ce soient vos objets connectés qui soient synchronisés dans une table MySQL nommée `objets`. Vous n'avez pas à synchroniser les données d'historique.
3. Testez le service Web à l'aide du testeur de requêtes REST. Assurez-vous d'avoir une réponse adéquate lors d'un ajout réussi, d'une modification réussie, d'une suppression réussie de même que lorsqu'une opération n'est pas réussie.
4. Conservez une copie du code du service Web dans le dossier `dev` de l'application SwiftUI.
