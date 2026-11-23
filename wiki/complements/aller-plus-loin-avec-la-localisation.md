# Écrire le fichier de localisation manuellement

La [génération automatique](../lecons/la-localisation-traduction.md#application-swiftui-bilingue) de la liste des chaînes à localiser est une fonctionnalité des plus intéressantes. Pourtant, il pourrait arriver que votre projet rencontre un problème pendant cette génération.

Si cela vous arrive, il est possible de générer cette liste manuellement.

- Dans le navigateur de projet de Xcode (s'il n'est pas visible, cliquez sur l'icône de chemise ![Icône chemise, filière](../lecons/images/Xcode-IconeChemise.png) dans la zone de gauche), faites un clic droit sur le dossier du projet (celui qui contient le fichier qui se termine par `App.swift`).
- Sélectionnez l'option **New File**.
- Le type du fichier doit être **Strings File** et le fichier doit absolument s'appeler `Localizable.strings`. Il s'agit du même nom de fichier que si les chaînes avaient été générées automatiquement puis importées au projet. Si vous avez plusieurs langues à supporter, chaque fichier portera ce même nom et sera placé dans un dossier dont le nom correspond à la langue suivi de `.lproj`, par exemple `en.lproj` ou `fr-CA.lproj`.
- Dans chacun des fichiers, vous devez entrer manuellement les chaînes à localiser, une ligne par chaîne. Chaque ligne sera au format :   

  ```text title="Fichier Localizable.strings"
  "Texte retrouvé dans le code" = "Valeur localisée";
  ```
- Pour localiser le nom de l'application ainsi que les valeurs que vous avez entrées dans Info.plist, pour chaque langue supportée, créez un nouveau fichier de localisation au même endroit que le premier. Le fichier doit s'appeler `InfoPlist.strings`.
- Cette fois, c'est le nom de chaque clé Info.plist que vous devez entrer ainsi que sa valeur localisée.

  ```text title="Fichier InfoPlist.strings"
  "CFBundleDisplayName" = "Valeur localisée";
  ```
