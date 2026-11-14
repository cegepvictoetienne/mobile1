# Exercice : S'approprier son mac  

!!! Note
    Puisque vous n'êtes pas administrateurs sur votre Mac, les applications installées à partir du Web devront être placées dans un dossier pour lequel vous possédez les droits d'écriture, par exemple `/users/monnom/Applications`. Si vous tentez de faire glisser le fichier .app dans le dossier Applications tel que le suggère la procédure habituelle, on vous demandera un mot de passe administrateur. Vous devrez plutôt faire un copier/coller manuel du fichier .app vers un dossier pour lequel vous possédez les droits d'écriture.

1. Modifiez le mot de passe de votre Mac.
2. Associez votre Mac à votre compte iCloud. Au besoin, créez un nouveau compte iCloud. Vous aurez besoin de ce compte pendant le développement de vos applications.
3. Branchez un second écran à votre Mac. Au besoin, configurez son emplacement et son comportement (ex : recopie vidéo ou pas) à l'aide des réglages système.
4. Sous votre dossier personnel (icône de maison dans la barre latérale du Finder), créez un dossier nommé `Applications`. C'est dans ce dossier que vous copierez les fichier **.app** lors de l'installation d'applications qui ne proviennent pas de l'AppStore.
5. À l'aide de l'icône de Wi-Fi dans le coin supérieur droit de l'écran, assurez-vous que votre Mac est branché au réseau sans fil **CEGEPVICTO** (les autres réseaux sans fil du Cégep sont généralement beaucoup plus lents).
6. Installez Google Chrome à partir du Web.
7. Configurez Google Chrome pour qu'il soit toujours dans le Dock.
8. Afin d'avoir quelques fichiers en place pour certaines manipulations, téléchargez ces fichiers dans votre dossier Téléchargements :  
    1. [Mac-CoucherDeSoleil.png](./fichiers/Mac-CoucherDeSoleil.png)  
    1. [Mac-CoucherDeSoleil.docx](./fichiers/Mac-CoucherDeSoleil.docx)  
    1. [Mac-CoucherDeSoleil.txt](./fichiers/Mac-CoucherDeSoleil.txt)  
9. À l'aide de Spotlight (⌘ Cmd +Espace ), ouvrez une fenêtre Terminal et entrez cette commande pour créer un fichier caché (qui débute par un point) :
    ```bash title="Terminal"
    touch ~/Downloads/.UnFichierCache.txt
    ```
10. Pour afficherles fichiers et dossiers cachés (ou les cacher s'ils étaient visibles), appuyez sur les touches ⌘ Cmd + ⇧ Maj + . dans le Finder.
11. Configurez le Finder pour afficher la barre du chemin d'accès.
12. Configurez le Finder pour faire la recherche à partir du dossier courant.
13. Configurez le Finder pour pouvoir voir « MacBook Pro de ... » dans la barre latérale. Il s'agit de l'équivalent
de « Ce PC » sous Windows.
14. Rendez-vous dans le menu  / ou Apple silicon (Apple Mx). À propos de ce Mac afin de vérifier si votre Mac a une puce Intel (Intel Core iX)
15. Installez Geany à partir du Web. Il sera utile lorsque vous désirerez ouvrir rapidement un seul fichier texte
(vous préférerez travailler avec Xcode pour programmer).
16. Associez les fichiers .txt à Geany.
17. Installez Devilbox. Vous en aurez besoin plus tard dans la session.  
    1. Le téléchargement peut être long, poursuivez les autres numéros pendant ce temps.  
    1. Notez que même avec une installation dans le dossier /users/monnom/Applications , vous aurez besoin d'un mot de passe admin lors de l'installation de Docker. Vous demanderez à votre prof de l'entrer pour vous lorsque requis.  
    1. Pour vous assurer que votre installation soit fonctionnelle, créez un fichier PHP qui fait un echo de "Hello World" (suivez les instructions dans la fiche d'installation de Devilbox).  
    
    Remarquez que [apical_lien_interne][fichier_sudoers,votre Mac a été configuré][/apical_lien_interne] pour vous permettre d'éditer le fichier hosts même si vous ne possédez pas les droits d'admin. Il suffit d'utiliser la commande suivante. Vous devez utiliser la commande telle quelle même si vous êtes déjà dans le dossier /etc.
        ```bash title="Terminal"  
        sudo nano /etc/hosts  
        ```    

18. Dans une fenêtre Terminal, lancez la commande which python3 pour voir où Python est installé par défaut sur macOS.   
19. Installez Seashore (éditeur d'images, icône de poisson bleu et blanc) à partir de l'AppStore.  
20. Ouvrez Seashore et agrandissez sa fenêtre sans cacher la barre de menu ni le Dock.  
21. Utilisez Seashore pour modifier la résolution de l'image téléchargée plus tôt.  
22. Installez Teams.  