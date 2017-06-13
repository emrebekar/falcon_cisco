from configs import *
from ssh import Ssh

import re
import json
import xml.etree.ElementTree as et

class Finder:
	__connect = None
	
	def __init__(self):
		self.__connect = Ssh(SSH_IP, SSH_USERNAME, SSH_PASSWORD)
		raw_response = self.__connect.sendCommand("config paging disable\n")
	
	def findSingleDevice(self, macAddress):
		if self.__connect != None:
			raw_response = self.__connect.sendCommand("show client summary\n")

			if raw_response != None:
				resp_array=raw_response.split('\n')
			
				for item in resp_array:
					if re.search(r'\b([0-9a-fA-F]{2}:??){5}([0-9a-fA-F]{2})\b', item):
						if macAddress in item:
							device_info = item.split(' ')
							data = {"MacAddress" : device_info[0].upper(), "AccessPoint" : device_info[1].upper()}
					
							json_data = json.dumps(data, encoding='UTF-8')
							return json_data
			else:
				return None

	def findMultipleDevices(self, devices):
		if self.__connect != None:
			raw_response = self.__connect.sendCommand("show client summary\n")

			if raw_response != None:
				resp_array=raw_response.split('\n')
				client_array = []
			
				for device in devices:
					mac_add = device['MacAddress'].upper()

					if mac_add != "00:00:00:00:00:00":
						for item in resp_array:
							if re.search(r'\b([0-9a-fA-F]{2}:??){5}([0-9a-fA-F]{2})\b', item):
								device_info = item.split(' ')

								#macaddress to uppercase
								device_info[0] = device_info[0].upper()
								device_info[1] = device_info[1].upper()

								if mac_add in device_info[0]:
									item_data = {"MacAddress" : device_info[0], "AccessPoint" : device_info[1]}
									client_array.append(item_data)
						
				if client_array != None:
					data = {"Clients":client_array} 
					json_data = json.dumps(data, encoding='UTF-8')
					return json_data
			
			else:
				return None
		else:
			return None

	def findAllDevices(self):
		if self.__connect != None:
			raw_response = self.__connect.sendCommand("show client summary")

			if raw_response != None:
				resp_array=raw_response.split('\n')
				
				client_array = []

				for item in resp_array:
					if re.search(r'\b([0-9a-fA-F]{2}:??){5}([0-9a-fA-F]{2})\b', item):		
						device_info = item.split(' ')
						item_data = {"MacAddress" : device_info[0].upper(), "AccessPoint" : device_info[1].upper()}
						client_array.append(item_data)
				
				if client_array != None:
					data = {"Clients":client_array} 
					json_data = json.dumps(data, encoding='UTF-8')
					return json_data
				
				else:
					return None

			else:
				return None
		else:
			return None
		

