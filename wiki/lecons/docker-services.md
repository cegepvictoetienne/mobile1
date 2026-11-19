# Services requis (en docker)

## Installation du Docker Compose  

### Installation

#### Installation de Docker Desktop (macOS)

Les services roule par-dessus Docker. Vous devez donc installer et démarrer Docker Desktop.

Téléchargement pour macOS : <https://docs.docker.com/desktop/install/mac-install/>

#### Installation des services (macOS)

Assurez-vous que [Git](https://git-scm.com/) soit installé sur votre poste de travail (il l'est par défaut sous macOS).

Sous macOS, ouvrez une fenêtre Terminal.

Placez-vous dans le dossier dans lequel vous désirez installer les services. Ici, j'ai choisi de le placer sous `Documents`.

```text title="Terminal"
cd /Users/monnom/Documents
```

Clonez le répertoire Git des services.

```text title="Terminal"
git clone https://github.com/cegepvictoetienne/mobile1_services.git
```

Placez-vous maintenant dans le nouveau dossier.

```text title="Terminal"
cd mobile1_services
```

Créez le fichier de configuration `.env` à partir de l'exemple fourni.

```text title="Terminal"
cp .env.example .env
```

### Configurations

Les configurations sont réalisées en éditant le fichier `.env`.


#### Configurations qui peuvent être laissées telles quelles

La majorité des configurations par défaut présentées dans le fichier `.env` peuvent être laissées telles quelles. 

### Démarrage des services

**Assurez-vous que Docker Desktop soit démarré**. Si vous omettez cette étape, vous obtiendrez le message « command not found: docker-compose ».

Dans une fenêtre Terminal, placez-vous dans le dossier `mobile1_services` puis lancez cette commande :

```text title="Terminal"
docker-compose up -d 
```

La première fois que la commande est exécutée, les fichiers requis seront téléchargés afin de créer les images Docker qui servent à démarrer les conteneurs.

Pour arrêter les conteneurs Docker, lancez la commande suivante :

```text title="Terminal"
docker-compose down
```

### Test de fonctionnememt

Si tout a fonctionné jusqu'ici, vous pouvez entrer l'adresse `http://127.0.0.1:5000` dans un navigateur.

### Projet helloworld

Pour créer votre premier site Web sous ce projet, modifiez les fichiers sous `app`. 

Dans ce dossier, modifiez app.py.


```python title="Fichier app/app.py"
@app.route("/")
def index():
    return jsonify(message="Hello, World!")
```

### Afficher le site Web dans un navigateur

Pour voir le résultat, entrer l'adresse `http://127.0.0.1:5000` dans un navigateur.

??? info "Pour plus d'information"

    « Manage data in Docker ». Docker. <https://docs.docker.com/storage/>
