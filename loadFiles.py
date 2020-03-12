import json
import requests

class LoadFiles(object):
	def __init__(self):
		super(LoadFiles, self).__init__()


	def getAllDatasCalendar(self):
		try:
			site    = "https://boldeagles.000webhostapp.com/calendario.php"
			local   = "http://localhost/apiCulturaJovem/calendario.php" 
			getApi  = requests.get(site)
			jsonGet = json.loads(getApi.text)
		except:
			jsonGet = ''
			
		return jsonGet
		
	def getIdDataCalendar(self, id):
		pass

	def postDataCalendar(self, json):
		pass