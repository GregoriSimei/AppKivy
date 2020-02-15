from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


class TelaManager(ScreenManager):
    pass

class Menu(Screen):

	def __init__(self, **kwargs):
		super(Menu, self).__init__(**kwargs)
		self.carregarCalendario()

	def carregarCalendario(self):
		print (self.manager)
		pass

class Culturajovem(App):
    def build(self):
        return TelaManager()


Culturajovem().run()

