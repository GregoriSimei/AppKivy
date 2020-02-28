import json
import requests
from datetime 							import date
from kivy.graphics 						import *
from kivy.graphics.vertex_instructions 	import *
from loadFiles 							import *
from kivy.app 							import App
from kivy.uix.screenmanager 			import Screen, ScreenManager
from kivy.uix.label 					import Label
from kivy.uix.boxlayout 				import BoxLayout
from kivy.uix.gridlayout 				import GridLayout
from kivy.lang 							import Builder
from kivy.uix.behaviors 				import ButtonBehavior
from kivy.animation 					import Animation


class TelaManager(ScreenManager):
    pass

class Menu(Screen):

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

	def addDinamicContentCalendar (self):

		evento = LoadFiles().getAllDatasCalendar()

		DIAS = [
		    'Seg',
		    'Ter',
		    'Qua',
		    'Qui',
		    'Sex',
		    'Sáb',
		    'Dom'
		]

		day = ""
		# Adiciona os textos nos widgets
		for datas in evento:

			if day != datas["date"]:
				dia = date(year=int(datas["date"][0:4]), month=int(datas["date"][5:7]), day=int(datas["date"][8:10]))
				mes = self.numMes(datas["date"][5:7])
				boxDataLayout	= BoxLayout(size_hint_y = None, height = 40)
				labelMonth		= Label(text = DIAS[dia.weekday()-1], size_hint_x = 0.2, bold = True, color = (0, 0, 0, 0.5))
				labelDayAndYear	= Label(text = datas["date"][8:10] + " " + mes + " " + datas["date"][0:4], font_size = '10sp', color = (0, 0, 0, 0.5), halign = "left")
				boxDataLayout.add_widget(labelMonth)
				boxDataLayout.add_widget(labelDayAndYear)
				self.ids.calendario_Scroll.add_widget(boxDataLayout)
				day = datas["date"]

			box 		= boxCalendarContanier()
			decoration 	= labelDecoration()
			hour 		= labelHourBox()
			title 		= boxTitleCalendar()
			box.add_widget(decoration)

			for data in datas:
				if data == "hour":
					hour.text = datas[data][0:5]
				if data == "title":
					title.labelTitle(datas[data])
				if data == "content":
					title.labelContent(datas[data])
			box.add_widget(hour)
			box.add_widget(title)

			self.ids.calendario_Scroll.add_widget(box)

class boxCalendarContanier(BoxLayout):
	pass

class labelHourBox(Label):
	pass

class boxTitleCalendar(ButtonBehavior, GridLayout):

	def __init__(self):
		super(boxTitleCalendar, self).__init__()
		self.apertado = False

	def on_release(self):
		if self.apertado: 
			anim = Animation(size=(self.width, 70), duration=0.2)
			anim.start(self)
			self.remove_widget(self.contentDate)
			self.contentTitle.bold = False
			self.apertado = False
		else:
			self.contentTitle.size_hint_y = None
			self.contentTitle.heigth = 70
			anim = Animation(size=(self.width, self.contentTitle.heigth + self.contentDate.texture_size[1]), duration=0.1)
			anim.start(self)
			anim.on_complete(self.add_widget(self.contentDate))
			self.contentTitle.bold = True
			self.apertado = True

	def labelTitle(self, title):
		label = Label()
		label.text = title
		self.contentTitle = label
		self.add_widget(label)

	def labelContent(self, content):
		label = labelContentCalendar()
		label.text = content
		self.contentDate = label

class labelDecoration(Label):
	pass	

class labelContentCalendar(Label):
	pass	

class Culturajovem(App):
    def build(self):
        return TelaManager()


Culturajovem().run()