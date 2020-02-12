from User import User
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label


class TelaManager(ScreenManager):
    pass

class Menu(Screen):
    pass


class Culturajovem2(App):
    def build(self):
        return TelaManager()


Culturajovem2().run()

