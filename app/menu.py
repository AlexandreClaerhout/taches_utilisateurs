from time import sleep
import os

class Menu:

    def __init__(self, heading:str, options:list[dict], parent:'Menu'= None):
        self._heading:str = heading
        for option in options:
            if isinstance(option['action'], self.__class__):
                option['action'].parent = self
        self._options:list[dict] = options
        self._parent = parent
    
    def _displayOptions(self, items:list[dict]):
        for item in items:
            self._displayItem(item)
        self._displayParent()
    
    def _displayParent(self):
        if isinstance(self.parent, Menu):
            print("[ENTER] Retour au menu précédent")
        else:
            print("[ENTER] Quitter")
        print('-'*40)

    def _displayItem(self, item:dict):
        print(f"{item['key']}. {item['label']}")
    
    def displayHeading(self, title:str):
        print(f'╭{'─'*40}╮')
        print(f'│{title.upper():^40}│')
        print(f'╰{'─'*40}╯')

    def _getChoice(self, options:list[dict]):
        choice:str = input("Quel est votre choix? ").strip()
        for option in options:
            if option['key'].upper() == choice.upper():
                return option['action']
        if choice == '':
            if isinstance(self.parent, self.__class__):
                return self.parent.render()
            else:
                return False
        print(f"Aucune option `{choice}` n'existe!")
        self._wait(2)
        self.render()

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value:'Menu' = None):
        self._parent = value

    def _clearConsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _wait(self, seconds:int=3):
        sleep(seconds)

    def render(self):
        self._clearConsole()
        self.displayHeading(self._heading)
        self._displayOptions(self._options)
        action = self._getChoice(self._options)
        if isinstance(action, self.__class__):
            action.render()
        elif callable(action):
            self._clearConsole()
            action(self)
        elif action == False:
            self._clearConsole()
            print('Ciao!')
            self._wait(2)
            self._clearConsole()
            quit()
        else:
            print("Erreur!!!")
