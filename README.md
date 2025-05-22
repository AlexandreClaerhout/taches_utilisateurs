## Prérequis

- Python
- Environnement virtuel
- SqlAlchemy
- Postgresql
- Git + Github/Gitlab

## Étapes de la mise en place du projet

1. Créer un dépôt dans Github
2. Créer un dossier local pour le projet
    ```bash
    mkdir taches-utilisateurs
    cd taches-utilisateurs
    ```
3. Y connecter le dépôt git distant
    ```bash
    git clone https://github.com/AlexandreClaerhout/taches_utilisateurs.git
    ```
4. Créer un fichier README et un dossier `docs`
    ```bash
    touch README.md
    mkdir docs
    ```
5. Ajouter au dossier `docs` le pdf d'explication
6. Préparer et effectuer le commit vers le dépôt distant
    ```bash
    git add README.md docs/Gestion\ d’utilisateurs\ et\ de\ tâches.pdf
    git commit -m "Ajout du README et d'un dossier docs contenant le pdf d'explication"
    git push origin main
    ```
7. Depuis la racine du dossier du projet, ouvrir VisualStudioCode
    ```bash
    code .
    ```
8. Dans VSC, ouvrir le terminal et y créer un environnement virtuel pour notre projet Python et l'activer
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
9. Une fois l'environnement virtuel activé, installer la librairie `sqlalchemy` et si nécessaire mettre à jour `pip`
    ```bash
    pip install --upgrade pip
    pip install sqlalchemy
    ```
10. Créer le fichier requirements.txt
    ```bash
    pip freeze > requirement.txt
    ```
11. Achever ce premier volet d'instructions en mettant à jour le dépôt Git
    ```bash
    git add README.md requirements.txt
    git commit -m "Modification du README et ajout du fichier requirements.txt"
    git push origin main
    ```
12. Ici, il s'agit d'un travail individuel. Mais il est bon de prendre l'habitude d'effectuer une mise à jour par rapport au dépôt central:

    ```bash
    git fetch origin main
    git pull origin main
    ```

13. Avant de clôturer cette partie, il reste une dernière chose à faire : renseigner les dossiers et/ou fichiers à écarter du dépôt git. Il faut ignorer le dossier `.venv`. Ouvrir le fichier `.gitignore` dans VSC et y ajouter le chemin du dossier `.venv`.

Jusqu'à présent tous les commits ont été effectués sur la branche main. Maintenant adoptons la bonne pratique de travailler sur une branche.


## Échafauder la structure de notre projet Python-SQLAlchemy

Ci-dessous, une vue complète de l'arborescence du projet.

```
projet
│
├── .git
├── .venv
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── alembic.ini
|
├── migrations/
|   |
|   ├── env.py
|   ├── README
|   ├── script.py.mako
|   └── versions/
|
├── docs/
|   |
|   └── Gestion d’utilisateurs et de tâches.pdf
|
└── app/
    │
    ├── config.py           # Configuration de la connexion à la base de données
    ├── db.py               # Initialisation de l'engine et de la session SQLAlchemy
    ├── main.py             # Application console (ajout, modification, listing, etc.)
    ├── menu.py             # Application menu 
    │
    ├── models/
    |   |
    |   ├── __init__.py     # Import des modèles pour faciliter l'accès
    |   ├── task.py         # Exemple de table : Tache
    |   └── user.py         # Exemple de table : Utilisateur
    |
    └── services/
        |
        └── __init__.py     # Import des modèles pour faciliter l'accès
```

​​1. Créer une nouvelle branche `projecttree` et basculer sur cette branche
    ```bash
    git checkout -b projecttree
    ```
2. Créer toute l'arborescence du dossier `app` et laisser les fichiers vides
    ```bash
    mkdir -p app/models app/services
    cd app
    touch config.py db.py main.py menu.py models/__init__.py services/__init__.py
    ```
    Les fichiers sont vides et ce n'est pas grave. L'important est d'avoir créé la structure.

    Si un dossier est vide, il suffit d'y créer un fichier `.gitkeep` pour que git prenne en compte ce dossier.
3. Effectuer le commit de la branche. Attention! On commit bien la branche `projecttree`
    ```bash
    git add README.md app/
    git commit -m "Création de la structure de l'application"
    git push -u origin projecttree
    ```
4. Aller sur Github et accepter le `pull request`
    ![Demande de pull request sur Github](docs/new_pull_resquest.png)

    Dans l'écran de gestion du pull request, le bandeau ci-dessous indique :
    - qu'il n'y a de prime abord aucun conflit
    - que la branche `projecttree` va être fusionnée avec la branche `main`

    ![alt text](docs/merge_banner.png)

    Il ne reste qu'à accepter la fusion en confirmant la création du pull request

    ![alt text](docs/create_pull_request.png)

5. L'écran suivant (qui normalement est accessible au merge master) propose de fusionner le pull request au `main`

    ![alt text](docs/merge_pull_request.png)

    Après avoir cliqué sur le bouton `Merge pull request`, un nouveau beandeau s'affiche proposant de modifier le message du commit

    ![alt text](docs/merge_pull_request_commit_message.png)

    Modifier le message si nécessaire. Puis confirme la fusion en cliquant sur `Confirm merge`.

    Un nouveau message indique que la fusion a été réalisée avec succès.

    ![alt text](docs/merge_pull_request_successful.png)

Ne pas oublier après avoir soumis les modifications de la branche `projecttree`, de basculer à nouveau sur la branche `main`. 
```bash
    git checkout main
```
Une fois sur la branche principale, mettre à jour celle-ci :
```bash
    git fetch
    git pull origin main
```

## Créer la base de données

### MSSQL

```sql
    USE master;
    GO
    IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'todo')
        CREATE DATABASE todo;
    END
    GO
    CREATE LOGIN todo_user WITH PASSWORD = 'Alfredisthebestbutler';
    GO
    CREATE USER todo_user FOR LOGIN todo_user;
    GO
    DENY VIEW ANY DATABASE TO todo_user; 
    GO
    ALTER AUTHORIZATION ON DATABASE::todo TO todo_user;
    GO
```

### POSTGRESQL

Effectuer les requêtes une à une.

```sql
    CREATE USER todo_user WITH PASSWORD 'Alfredisthebestbutler';
    CREATE DATABASE todo WITH OWNER=todo_user;
    GRANT ALL PRIVILEGES ON DATABASE todo TO todo_user;
```

### MYSQL/MARIADB

```sql
    CREATE DATABASE IF NOT EXISTS todo;
    CREATE USER 'todo_user'@'%' IDENTIFIED BY 'Alfredisthebestbutler';
    GRANT SELECT, INSERT, UPDATE, DELETE ON todo.* TO 'todo_user'@'%';
    FLUSH PRIVILEGES;
```

## Driver

Afin de permettre à Python de communiquer avec la base de données Postgresql, il faut installer le driver `psycopg2`.

```bash
    pip install psycopg2
```

## Alembic et révisions

1. Installer `Alembic`

```bash
    pip install alembic
```

2. Créer le dossier `migrations` et les fichiers de configuration (alembic.ini, env.py). Effectuer ceci à la racine du projet.

```bash
    alembic init migrations
```

3. Dans le fichier `alembic.ini`, modifier le paramètre `sqlalchemy.url` comme suit :

```bash
    # database URL.  This is consumed by the user-maintained env.py script only.
    # other means of configuring database URLs may be customized within the env.py
    # file.
    sqlalchemy.url = postgresql://todo_user:Alfredisthebestbutler@91.86.128.80:15432/todo
```

### Créer une révision

Chaque révision est écrite dans un script. Chaque script contient 2 fonctions : `upgrade` et `downgrade`.

Pour créer un nouveau fichier révision, exécuter le code suivant:

```bash
    alembic revision -m "Creation de la table User"
```

Cela rappelle vaguement qqch, non? Git peut-être?

Attention à ne pas utiliser de caractères accentués ou spéciaux pour écrire le message: le message sert à construire le nom du fichier de révision.

Un nouveau fichier est créé dans le dossier `migrations/versions/`. 

Ouvrir le fichier et compléter les scripts.

```bash
def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'user',
        Column("id", INTEGER, primary_key=True),
        Column('username', VARCHAR(50), nullable=False),
        Column('email', VARCHAR(100), nullable=False),
        Column('password', TEXT, nullable=False),
        Column('is_active', BOOLEAN, default=False)
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user')
```

La fonction `upgrade` permet d'avancer dans l'historique de migration. Alors que la fonction `downgrade` effectue une marche arrière dans l'historique. Cela signifie que chaque action réalisée dans la fonction `upgrade` doit avoir son action exacte opposée dans la fonction `downgrade`

Pour mettre à jour la migration et effectuer toutes les révisions encore non-exécutées, lancer la commande:
```bash
    alembic upgrade head
```

Pour migrer réversiblement, exécuter la commande:
```bash
    alembic downgrade -1
```
Cette commande va reculer d'une révision dans l'historique de la migration.

Quelques autres commandes qu'il est bon de connaître:
- `alembic history` : Afficher l'historique des révisions
- `alembic merge` : Créer un nouveau script de révision en fusionnant deux ou plusieurs révisions
- `alembic edit` : Ouvrir le script de révision actuelle dans un éditeur
- `alembic current` : Afficher la dernière révision effectuée 

Avant de terminer cette partie concernant `Alembic`, exécuter la révision que nous avons écrite.

```bash
    alembic upgrade head
```

Tout se passe bien.

```
    INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
    INFO  [alembic.runtime.migration] Will assume transactional DDL.
    INFO  [alembic.runtime.migration] Running upgrade  -> 92084a9ee8b5, Creation de la table User
```

Dans la base de données, on constate que 2 tables y ont été créées :
- La table `user` évidemment;
- Et la table `alembic_version` qui contient l'historique des révisions effectuées sur la db.

Cette dernière table permet à `alembic` de ne pas exécuter à nouveau le même script. 