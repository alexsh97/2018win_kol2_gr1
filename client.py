class client:

	def __init__(self,client_name,client_ID, client_money):
		self.name = client_name
		self.ID = client_ID
		self.money = client_money

	def showInfo(self):
		print("Name: "+self.name)
