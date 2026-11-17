# Exercice 4 : Un peu de raffinement et questions théoriques

Cet exercice se déroule en deux parties.

1. Demandez à votre prof de vous remettre une feuille avec les questions théoriques. Répondez-y en équipe de deux.
2. Vous devez poursuivre le développement de votre application [Devine le nombre](devine-le-nombre.md).

    !!! Note
        Dans cet exercice et dans les autres à venir dans la session, si vous utilisez un outil d'IA pour générer une image, vous devez ajouter une note en bas de page à cet effet dans l'écran de l'application.

    1. Ajoutez un titre dans la barre de navigation de votre application. Vous n'avez pas besoin de placer quoi que ce soit à gauche ni à droite du titre. Suggestion : pour mieux vous y retrouver dans votre code, ajoutez un commentaire pour identifier l'accolade qui referme le `VStack` et celle qui referme le `NavigationStack`.
    2. Ajoutez un AppIcon. Dans le simulateur, cliquez sur l'icône de maison pour voir l'icône associée à l'application.
    3. Configurez la couleur d'accent de l'application. Ce pourrait être, par exemple, un orange punché ou un fuchsia. Le bouton de soumission doit utiliser cette couleur. Libre à vous de l'utiliser pour autre chose.
    4. Configurez une autre couleur personnalisée qui sera utilisée comme couleur de fond qui recouvre tout l'écran, par exemple une nuance de gris. Vérifiez le résultat quand l'application est en mode sombre et en mode clair.
    5. Afin de tester vos techniques de débogage, faites afficher dans la sortie standard le nombre généré. Une fois le test complété, mettez ce code en commentaire. Avez-vous pensé utiliser un raccourci-clavier?
    6. Le traitement effectué par le bouton de soumission doit être placé dans une fonction. N'oubliez pas de documenter cette fonction.
    7. Lorsque l'application donne une rétroaction à l'usager, elle doit afficher une image en plus du texte.
        1. L'image doit être un ajout visuel pour que l'usager comprenne que sa réponse est correcte, trop grande ou trop petite.
        2. À vous de trouver les images appropriées. Assurez-vous qu'elles soient libres de droits.
        3. Suggestion : une montagne quand le nombre est trop grand, une vallée quand le nombre est trop petit et un soleil quand le nombre est deviné.
        4. Important : s'il s'agit d'images sous licence Creative Commons, vous devez afficher l'attribution de l'image :

            > Attribution — Vous devez créditer l'Œuvre, intégrer un lien vers la licence et indiquer si des modifications ont été effectuées à l'Oeuvre.[^1]

        5. Dès que l'usager commence à modifier le texte dans le `TextField`, l'image doit disparaître.
        6. Astuce : pour ne pas que le contenu de l'écran bouge verticalement quand l'image apparaît ou disparaît, vous pouvez réserver la hauteur de la zone comme suit :

            ```swift title="SwiftUI"
            ZStack {
              if ... {
                Image(...)
                  .resizable()
                  .scaledToFit()
              }
            }
            .frame(height: 100)  // le ZStack aura toujours cette hauteur
            ```

    8. **OPTIONNEL** : utilisez un outil de traitement d'images, par exemple Seashore (disponible sur le App Store) pour ajouter un calque par-dessus chaque image. L'image affichée quand le nombre est trop grand aura un calque orangé et l'image pour un nombre trop petit aura un calque bleu. Jouez avec le mode de fusion du calque (*blending*) jusqu'à l'obtention d'un résultat satisfaisant.
    9. Vous devez garder un historique des réponses données par l'usager. Donc, à chaque fois qu'une réponse est soumise, elle doit être ajoutée à un tableau.
    10. Le tableau des réponses, ainsi que leur statut (trop grand, trop petit ou correct) doit être affiché en tout temps dans le bas de l'écran. Ne vous souciez pas pour l'instant de ce qui arrive si le tableau prend trop de place à l'écran.
    11. **OPTIONNEL** : plutôt que d'afficher toutes les réponses entrées, affichez seulement les deux qui sont le plus près de la valeur recherchée : celle en-dessous et celle au-dessus.

[^1]: « Attribution 4.0 International (CC BY 4.0) ». Creative Commons. <https://creativecommons.org/licenses/by/4.0/deed.fr>
