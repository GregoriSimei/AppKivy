from kivy.app 				import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label 		import Label
from kivy.uix.boxlayout 	import BoxLayout
import json


class TelaManager(ScreenManager):
    pass

class Menu(Screen):

	def calendario(self):
		arq   = open('./arq/calendario.json','r')
		try:
			print ("entrou - abriu arquivo")
			print (arq)
			datas = json.load(arq)
			print (datas)
			print("não deu erro ")
			for data in datas:
				for label in data:
					if label == "horario":
						self.ids.calendario_Scroll.add_widget(Label(text=data[label], size_hint_y=None, height=200, color=(0,0,0,1)))
			print ("leu")
		except:
			arq.close()
			print("deu erro - fechou arquivo")
		else:
			arq.close()
			print("terminou com exito - fechou arquivo")
		'''calendario = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
		for texto in calendario:
			self.ids.calendario_Scroll.add_widget(Label(text=texto, size_hint_y=None, height=200, color=(0,0,0,1)))'''

	def dinamicContentCalendar (self):
		pass

class Culturajovem(App):
    def build(self):
        return TelaManager()


Culturajovem().run()

