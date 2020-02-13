from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


class TelaManager(ScreenManager):
    pass

class Menu(Screen):
	def carregarCalendario(self):
		pass

class Culturajovem(App):
    def build(self):
        return TelaManager()


Culturajovem().run()

