import json
import requests
from kivy.app 							import App
from kivy.uix.screenmanager 			import Screen, ScreenManager
from kivy.uix.label 					import Label
from kivy.uix.boxlayout 				import BoxLayout
from kivy.graphics 						import *
from kivy.graphics.vertex_instructions 	import *
from kivy.lang 							import Builder


class TelaManager(ScreenManager):
    pass

class Menu(Screen):


	def calendario(self):
		arq   = open('./arq/calendario.json','w')
		try:
			getApi = requests.get("https://boldeagles.000webhostapp.com/calendario.php")
			arq.write(json.dumps(getApi.text))
			jsonGet = json.loads(getApi.text)
			for data in jsonGet :
				self.dinamicContentCalendar(data)
		except:
			arq.close()
		else:
			arq.close()

	def dinamicContentCalendar (self, evento):

		def update_rect(instance, value):
		    instance.rect.pos = instance.pos
		    instance.rect.size = instance.size

		# Container base para ser montado a parte gráfica de cada bloco do calendario
		boxContainer = BoxLayout()
		boxContainer.size_hint_y = None
		boxContainer.width = 170
		boxContainer.padding = '5sp'

		# Apenas enfeite que ficara a direita, dentro do boxContainer
		leftLineInsideBoxContainer = Label()
		leftLineInsideBoxContainer.size_hint_x = 0.02
		with leftLineInsideBoxContainer.canvas:
			Color(rgba = (0.65, 0.65, 0.65, 1))
			leftLineInsideBoxContainer.rect = Rectangle(pos  = (leftLineInsideBoxContainer.x+(leftLineInsideBoxContainer.width*1.5)/2, leftLineInsideBoxContainer.y), 
					  									size = (leftLineInsideBoxContainer.width/500, leftLineInsideBoxContainer.height))
			Color(0.8, 0.8, 0.8,1)
			'''
			Ellipse(pos = (leftLineInsideBoxContainer.x, leftLineInsideBoxContainer.y+(leftLineInsideBoxContainer.height/2)-(leftLineInsideBoxContainer.width/2)), 
					size = (leftLineInsideBoxContainer.width*1.5, leftLineInsideBoxContainer.width*1.5))
			'''

		# Altera o tamanho e a posição do widget leftLineInsideBoxContainer
		leftLineInsideBoxContainer.bind(pos=update_rect, size=update_rect)

		# No hourBox estará contida a hora do envento
		hourBox = Label()
		hourBox.font_size = '10sp'
		hourBox.color = (0, 0, 0, 0.5)
		hourBox.size_hint_x = 0.2

		# No titleBox estará contido o titulo do evento
		titleBox = Label()
		with titleBox.canvas.before: 
			Color(rgba = (0, 0.5, 0.9, 1))
			titleBox.rect = RoundedRectangle(size = boxContainer.size, 
											 pos = titleBox.pos, 
											 radius = [(10.0, 10.0), (10.0, 10.0), (10.0, 10.0), (10.0, 10.0)])

		# Muda o tamanho e a posição do widget titleBox
		titleBox.bind(pos=update_rect, size=update_rect)

		# Adiciona os textos nos widgets
		for data in evento:
			if data == "hour":
				hourBox.text = evento[data][0:5]
			if data == "title":
				titleBox.text = evento[data]

		boxContainer.add_widget(leftLineInsideBoxContainer)
		boxContainer.add_widget(hourBox)
		boxContainer.add_widget(titleBox)

		self.ids.calendario_Scroll.add_widget(boxContainer)


class Culturajovem(App):
    def build(self):
        return TelaManager()


Culturajovem().run()

