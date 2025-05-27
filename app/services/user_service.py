class UserService:
    
    def __init__(self):
        pass

    def list(self, menu):
        menu.displayHeading('Liste des utilisateurs')
        self.backToMenu(menu)

    def add(self, menu):
        menu.displayHeading('Ajouter un utilisateur')
        self.backToMenu(menu)

    def remove(self, menu):
        menu.displayHeading('Supprimer un utilisateur')
        self.backToMenu(menu)
    
    def backToMenu(self,menu):
        input("ENTER to return to menu")
        menu.render()