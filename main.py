from kivy.app 				import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label 		import Label
from kivy.uix.boxlayout 	import BoxLayout
from kivy.graphics import *
from kivy.graphics.vertex_instructions import *
import json


class TelaManager(ScreenManager):
    pass

class Menu(Screen):


	def calendario(self):
		arq   = open('./arq/calendario.json','r')
		try:
			print ("entrou - abriu arquivo")
			datas = json.load(arq)
			print("não deu erro ao ler arquivo")
			print("Enviando arquivo")
			for data in datas :
				self.dinamicContentCalendar(data)	
			print ("leu o arquivo")
		except:
			arq.close()
			print("deu erro - fechou arquivo")
		else:
			arq.close()
			print("terminou com exito - fechou arquivo")

	def dinamicContentCalendar (self, evento):

		print("começou a criar parte gráfica")

		# Container base para ser montado a parte gráfica de cada bloco do calendario
		boxContainer = BoxLayout()
		boxContainer.size_hint_y = None
		boxContainer.width = 200
		boxContainer.padding = '10sp'
		print("terminou de criar o boxContainer")

		# Apenas enfeite que ficara a direita, dentro do boxContainer
		leftLineInsideBoxContainer = Label()
		leftLineInsideBoxContainer.size_hint_x = 0.02
		with leftLineInsideBoxContainer.canvas:
			print("Começou a criar o canvas")
			Color(rgba = (0.65, 0.65, 0.65, 1))
			print("estabeleceu uma cor")
			Rectangle(pos = (leftLineInsideBoxContainer.x+(leftLineInsideBoxContainer.width*1.5)/2, leftLineInsideBoxContainer.y), 
					  size = (leftLineInsideBoxContainer.width/10, leftLineInsideBoxContainer.height))
			print("criou o retangulo")
			Color(0.8, 0.8, 0.8,1)
			Ellipse(pos = (leftLineInsideBoxContainer.x, leftLineInsideBoxContainer.y+(leftLineInsideBoxContainer.height/2)-(leftLineInsideBoxContainer.width/2)), 
					size = (leftLineInsideBoxContainer.width*1.5, leftLineInsideBoxContainer.width*1.5))
		print("Terminou de criar leftLineInsideBoxContainer")

		# No hourBox estará contida a hora do envento
		hourBox = Label()
		hourBox.color = (0, 0, 0, 0.5)
		hourBox.size_hint_x = 0.2
		print("terminou de criar hourBox")

		# No titleBox estará contido o titulo do evento
		titleBox = Label()
		titleBox.canvas.before.add(Color(rgba = (0, 0.5, 0.9, 1)))
		titleBox.canvas.before.add(RoundedRectangle(size = titleBox.size, 
													pos = titleBox.pos, 
													radius = [(10.0, 10.0), (10.0, 10.0), (10.0, 10.0), (10.0, 10.0)]))
		print("Terminou de criar titleBox")

		for data in evento:
			print("entrou para adicionar text para as labels")
			print(data)
			if data == "horario":
				hourBox.text = evento[data]
			if data == "titulo":
				titleBox.text = evento[data]
			print("Terminou de adcionar o text")

		print("Começando a adicionar widgets no boxContainer")
		'''boxContainer.add_widget(leftLineInsideBoxContainer)
		boxContainer.add_widget(hourBox)'''
		boxContainer.add_widget(titleBox)
		print("Terminou de adicionar widgets no boxContainer")

		self.ids.calendario_Scroll.add_widget(boxContainer)


class Culturajovem(App):
    def build(self):
        return TelaManager()


Culturajovem().run()

