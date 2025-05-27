from menu import Menu
from services import UserService

def sampleAction(menu):
    print("Super")
    input("Enter to return to menu")
    menu.render()

def showMenu():

    userservice:UserService = UserService()
    task:Menu = Menu("Menu tâche", [
        {'key': '1', 'label': 'Ajouter', 'action': sampleAction},
        {'key': '2', 'label': 'Supprimer', 'action': sampleAction},
        {'key': '3', 'label': 'Lister', 'action': sampleAction},
    ])

    user:Menu = Menu("Menu utilisateur", [
        {'key': '1', 'label': 'Ajouter', 'action': userservice.add},
        {'key': '2', 'label': 'Supprimer', 'action': userservice.remove},
        {'key': '3', 'label': 'Lister', 'action': userservice.list},
    ])

    main = Menu("Menu principal", [
        {'key': '1', 'label': 'Utilisateur', 'action': user},
        {'key': '2', 'label': 'Tâche', 'action': task},
    ])

    main.render()

def main():
    showMenu()

main()