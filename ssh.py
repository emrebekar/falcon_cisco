import paramiko
import time
import re
import socket

from configs import *

class Ssh:
	ssh_client = None
	console = None
	
	def __init__(self, address, username, password):	
		while 1:
			try:
				self.ssh_client = paramiko.SSHClient()
				self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				self.ssh_client.connect(address, username=username, password=password, look_for_keys=False, allow_agent=False)
				self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				self.console = self.ssh_client.invoke_shell()
				self.console.keep_this = self.ssh_client
				
				self.console.send(username+'\n')
				time.sleep(1)
				#resp = self.console.recv(9999)
				#print resp
				
				self.console.send(password+'\n')
				time.sleep(1)
				#resp = self.console.recv(9999)
				#print resp
				
				break
				
			except:
				print "Attempting to reconnect to the Cisco Network!!!"
				continue
			
		
	def sendCommand(self, cmd):
		if(self.ssh_client):

			self.console.send(cmd+'\n')
			time.sleep(1)
			raw_resp = self.console.recv(65535)
		
			#print raw_resp
			return raw_resp
		else:
			return None
			
	def closeConnection(self):
		if ssh_client != None:
			ssh_client.close()