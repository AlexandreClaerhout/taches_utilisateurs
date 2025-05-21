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