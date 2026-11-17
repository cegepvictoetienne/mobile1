# Exercice 9 : Tables liées

1. Vous devez maintenant afficher pour chaque objet la dernière valeur stockée dans la table des historiques. Cette information est considérée comme la valeur actuelle de l'objet connecté. Pistes de solution :
    1. L'historique d'un objet est disponible directement à l'aide de `objet.historiques` (ajustez le nom de la variable `objet` et de sa propriété `historiques` selon votre code).
    2. Les données d'historiques doivent être triées en ordre de date afin d'avoir la date la plus récente en premier.
    3. La valeur d'historique la plus récente sera dans `objet.historiques.first`.
    4. Votre code doit réagir correctement si jamais un objet n'avait pas d'historique.
    5. Je vous suggère d'ajouter une propriété calculée ou encore une méthode dans le modèle `Objet` pour obtenir la valeur recherchée.
2. Dans le cas d'une valeur booléenne, faites le nécessaire pour afficher un mot du genre « ouverte » ou « fermée » plutôt que 0 ou 1.
3. **OPTIONNEL** : affichez une icône différente pour les valeurs booléennes selon qu'elles sont à `true` ou à `false` (ex : ampoule blanche si allumée, ampoule noire si éteinte).
4. **OPTIONNEL** : prévoyez un mécanisme pour afficher l'unité de mesure (ex : C, lumens).
5. Prenez le temps d'affiner l'apparence de votre application :
    1. Configurez la couleur d'accent de votre application ou au moins une couleur personnalisée.
    2. Testez votre application en mode Sombre et en mode Clair et effectuez les ajustements nécessaires si requis. Au besoin, codez une couleur d'accent ou une couleur personnalisée différente pour chacun des modes.
    3. Ajoutez une AppIcon à votre application.
    4. Donnez à votre application un **Display Name** approprié.
6. Testez votre application sur un iPhone.
7. Récupérez les données de l'application à partir du iPhone et explorez les fichiers du paquet téléchargé.
8. Faites une impression d'écran des données du iPhone où l'on voit que les clés étrangères sont bien remplies. Placez l'impression d'écran dans le dossier `dev` de l'application. Ce type de manipulation pourrait être demandé en examen.
