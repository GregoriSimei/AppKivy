import json
import requests

class LoadFiles(object):
	def __init__(self):
		super(LoadFiles, self).__init__()


	def getAllDatasCalendar(self):
		arq   = open('./arq/calendario.json','w')
		try:
			getApi = requests.get("https://boldeagles.000webhostapp.com/calendario.php")
			arq.write(json.dumps(getApi.text))
			jsonGet = json.loads(getApi.text)
		except:
			arq.close()
			jsonGet = '{"Nothing"}'
		else:
			arq.close()

		return jsonGet
		
	def getIdDataCalendar(self, id):
		pass

	def postDataCalendar(self, json):
		pass