import json
import requests
from loadFiles 							import *
from kivy.app 							import App
from kivy.uix.screenmanager 			import Screen, ScreenManager
from kivy.uix.label 					import Label
from kivy.uix.boxlayout 				import BoxLayout
from kivy.graphics 						import *
from kivy.graphics.vertex_instructions 	import *
from kivy.lang 							import Builder
from kivy.uix.behaviors 				import ButtonBehavior
from kivy.animation 					import Animation


class TelaManager(ScreenManager):
    pass

class Menu(Screen):

	def calendario(self):

		apiGet = LoadFiles().getAllDatasCalendar()
		self.addDinamicContentCalendar(apiGet)
		
	def numMes (self, num):
			mes = ""
			if num == "01":
				mes = "Jan"
			elif num == "02":
				mes = "Fev"
			elif num == "03":
				mes = "Mar"
			elif num == "04":
				mes = "Abr"
			elif num == "05":
				mes = "Mar"
			elif num == "06":
				mes = "Mai"
			elif num == "07":
				mes = "Jun"
			elif num == "08":
				mes = "Jul"
			elif num == "09":
				mes = "Ago"
			elif num == "10":
				mes = "Set"
			elif num == "11":
				mes = "Out"
			elif num == "12":
				mes = "Nov"
			return mes

	def addDinamicContentCalendar (self, evento):

		date = ""
		# Adiciona os textos nos widgets
		for datas in evento:

			if date != datas["date"]:
				mes = self.numMes(datas["date"][5:7])
				boxDataLayout	= BoxLayout(size_hint_y = None, height = 40)
				labelMonth		= Label(text = mes, size_hint_x = 0.2, bold = True, color = (0, 0, 0, 0.5))
				labelDayAndYear	= Label(text = datas["date"][8:10] + ", " + datas["date"][0:4], font_size = '10sp', color = (0, 0, 0, 0.5))
				boxDataLayout.add_widget(labelMonth)
				boxDataLayout.add_widget(labelDayAndYear)
				self.ids.calendario_Scroll.add_widget(boxDataLayout)
				date = datas["date"]

			box 		= boxCalendarContanier()
			decoration 	= labelDecoration()
			hour 		= labelHourBox()
			title 		= labelTitleCalendar()
			box.add_widget(decoration)

			for data in datas:
				if data == "hour":
					hour.text = datas[data][0:5]
				if data == "title":
					title.text = datas[data]
			box.add_widget(hour)
			box.add_widget(title)

			self.ids.calendario_Scroll.add_widget(box)

class boxCalendarContanier(ButtonBehavior, BoxLayout):
	def __init__(self):
		super(boxCalendarContanier, self).__init__()
		self.size_hint_y = None
		self.height = 70
		self.padding = '5sp'
		self.apertado = False

	def on_release(self):
		if self.apertado: 
			anim = Animation(size=(self.width, 70), duration=0.3)
			anim.start(self)
			self.apertado = False
		else:
			anim = Animation(size=(self.width, 170), duration=0.3)
			anim.start(self)
			self.apertado = True

class labelHourBox(Label):
	def __init__(self):
		super(labelHourBox, self).__init__()
		self.font_size = '10sp'
		self.color = (0, 0, 0, 0.5)
		self.size_hint_x = 0.2

class labelTitleCalendar(Label):
	def __init__(self):
		super(labelTitleCalendar, self).__init__()
		def update_rect(instance, value):
			instance.rect.pos = instance.pos
			instance.rect.size = instance.size
		with self.canvas.before: 
			Color(rgba = (0, 0.5, 0.9, 1))
			self.rect = RoundedRectangle(size = self.size, 
											 pos = self.pos, 
											 radius = [(10.0, 10.0), (10.0, 10.0), (10.0, 10.0), (10.0, 10.0)])

		# Atualiza o tamanho e a posição do widget self
		self.bind(pos=update_rect, size=update_rect)

class labelDecoration(Label):
	def __init__(self):
		super(labelDecoration, self).__init__()
		def update_rect(instance, value):
			instance.rect.pos = instance.pos
			instance.rect.size = instance.width/4, instance.height

		self.size_hint_x = 0.02
		with self.canvas:
			Color(rgba = (0.65, 0.65, 0.65, 1))
			self.rect = Rectangle(pos  = (self.x+(self.width*1.5)/2, self.y), 
					  			  size = (self.width/500, self.height))
			'''
			Ellipse(pos = (self.x, self.y+(self.height/2)-(self.width/2)), 
					size = (self.width*1.5, self.width*1.5))
			'''

		# Altera o tamanho e a posição do widget
		self.bind(pos = update_rect, size = update_rect)

class Culturajovem(App):
    def build(self):
        return TelaManager()


Culturajovem().run()