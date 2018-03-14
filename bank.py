
from client import client

class bankc:
	
	def __init__(self,bank_name):
		self.bank_name = bank_name
		self.numOfClient = 0
		
		

	def addClient(self,client_name, client_ID, client_money):
		new_client = client(client_name,client_ID,client_money)
		self.numOfClient += 1
		
	
	def listOfClient(self):
		for c in self.clients:
			c.showInfo()
			

	def addMoneyToClient(self,client_id, money):
		


	
