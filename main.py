from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label


class TelaManager(ScreenManager):
    pass

class Menu(Screen):

	def __init__(self, **kwargs):
		super(Menu, self).__init__(**kwargs)
		self.carregarCalendario()

	def carregarCalendario(self):
		pass

class Culturajovem(App):
    def build(self):
        return TelaManager()


Culturajovem().run()

