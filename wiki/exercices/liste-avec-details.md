# Exercice 10 : Liste avec détails

Votre liste d'objets connectés doit permettre de cliquer sur un objet afin d'obtenir la liste des valeurs d'historique qui lui sont associées.

Vous devez respecter ces consignes :

1. Placez le code des barres d'outils [dans son propre fichier](../lecons/la-barre-de-navigation.md), dans un sous-dossier nommé `Views`. Notez que si la barre d'outils a besoin de préférences utilisateur, il suffit d'y redéclarer la variable avec `@AppStorage`.
2. Un clic sur un objet fait apparaître une vue enfant qui contient l'historique complet de l'objet. Assurez-vous que les données soient affichées en ordre chronologique peu importe leur ordre dans la base de données.
3. Dans l'historique, les valeurs booléennes doivent afficher un mot du genre « Ouverte » ou « Fermée » plutôt que 0 ou 1.
4. Pour chaque objet connecté, ajoutez une icône pour éditer l'objet et une autre pour le supprimer. Pour l'instant, un clic sur une de ces icônes affichera simplement un message dans la sortie standard à l'aide de `print()`.
5. Apportez un soin quasi-maladif à l'apparence de votre application!
6. N'oubliez pas de bien documenter les paramètres et valeurs de retour des méthodes que vous écrivez.
7. Assurez-vous que chaque vue, incluant le fichier `ContentView.swift`, soit placée dans le sous-dossier `Views`.
8. Afin d'alléger votre vue principale, déplacez dans un fichier distinct tout le code qui permet d'afficher les données d'un objet connecté. Votre vue principale aura subi un régime de minceur, par exemple :

    ```swift title="ContentView.swift"
    List (objets) { objet in
      NavigationLink(value: objet) {
        DonneesObjet(objet: objet)
      }
    }
    ...
    ```

9. Assurez-vous que chaque vue enfant ait un titre qui indique clairement ce qui est affiché.
10. La barre d'outils doit apparaître et être fonctionnelle sur chaque vue.
11. Prenez le temps de soigner les `#Preview` de chacune de vos vues.
12. Faites le nécessaire pour que les liens ou icônes dans les barres d'outils dans le haut et dans le bas de l'écran ne soient pas en bleu. À vous de trouver une technique pour ne pas avoir à répéter la couleur à chacun des liens ou icônes.
