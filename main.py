from finder import Finder

import falcon
import json

class FindAllDevices:
	def on_get(self, req, resp):		
		finder = Finder()
		resp.status = falcon.HTTP_200
		resp.set_header('Access-Control-Allow-Origin','*')
		resp.body = (finder.findAllDevices())

class FindSingleDevice:
	def on_post(self, req, resp):
		finder = Finder()	
		raw = req.stream.read()
		data = json.loads(raw)
		
		resp.status = falcon.HTTP_200
		resp.set_header('Access-Control-Allow-Origin','*')
		resp.body = (finder.findSingleDevice(data['MacAddress']))
		
class FindMultipleDevices:
	def on_post(self, req, resp):
		finder = Finder()
		raw = req.stream.read()
		data = json.loads(raw)
		
		resp.status = falcon.HTTP_200
		resp.set_header('Access-Control-Allow-Origin','*')
		resp.body = (finder.findMultipleDevices(data['Clients']))

class Deneme:
	def on_post(self, req, resp):
		print "Deneme"
		resp.status = falcon.HTTP_200
		resp.body = (req.stream.read())

app = falcon.API()
app.add_route('/findalldevices', FindAllDevices())
app.add_route('/findsingledevice', FindSingleDevice())
app.add_route('/findmultipledevices', FindMultipleDevices())
app.add_route('/deneme', Deneme())
