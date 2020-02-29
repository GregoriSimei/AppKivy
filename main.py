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
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty


class TelaManager(ScreenManager):
    pass

class Menu(Screen):

	def addDinamicContentCalendar (self):

		jsonRequest = LoadFiles().getAllDatasCalendar()

		DAYS = ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom']
		MONTHS = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

		day = ""

		for jsonUnitData in jsonRequest:

			if day != jsonUnitData["date"]:
				dia = date(year=int(jsonUnitData["date"][0:4]), month=int(jsonUnitData["date"][5:7]), day=int(jsonUnitData["date"][8:10]))
				mes = MONTHS[int(jsonUnitData["date"][5:7])-1]
				boxDataLayout	= BoxLayout(size_hint_y = None, height = 40)
				labelMonth		= Label(text = DAYS[dia.weekday()-1], size_hint_x = 0.2, bold = True, color = (0, 0, 0, 0.5))
				labelDayAndYear	= Label(text = jsonUnitData["date"][8:10] + " " + mes + " " + jsonUnitData["date"][0:4], font_size = '10sp', color = (0, 0, 0, 0.5), halign = "left")
				boxDataLayout.add_widget(labelMonth)
				boxDataLayout.add_widget(labelDayAndYear)
				self.ids.calendario_Scroll.add_widget(boxDataLayout)
				day = jsonUnitData["date"]

			box 		= boxCalendarContanier()
			decoration 	= labelDecoration()
			hour 		= labelHourBox()
			title 		= boxTitleCalendar()
			box.add_widget(decoration)

			for evento in jsonUnitData:
				if evento == "hour":
					hour.text = jsonUnitData[evento][0:5]
				if evento == "title":
					title.labelTitle(jsonUnitData[evento])
				if evento == "content":
					title.labelContent(jsonUnitData[evento])
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

class SurroundingSlider(Widget):
	# value é para o circulo de baixo
    value = NumericProperty(0.5)

    # angle_start é para o circula de traz
    angle_start = NumericProperty(360)

    segments = NumericProperty(50)

    angle_stop = NumericProperty(33)

    radius = NumericProperty(20)

    bar_width = NumericProperty(10)

    cap_length = NumericProperty(30)

    cap_texture_cut = NumericProperty(.2)
    min = NumericProperty(0)
    max = NumericProperty(1)
    a = NumericProperty(0)
    texture_back = StringProperty('fundo.png')
    texture_fill = StringProperty('fundo2.png')

Culturajovem().run()