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
