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
7. 
