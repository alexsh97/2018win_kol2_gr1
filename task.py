import json

#1
def addBank(bank_name):
	global allBanks
	try:
		if bank_name not in allBanks:
			allBanks[bank_name] = {}
		else:
			raise Exception("Error:"+bank_name+" already exist'!\n Here is the bank menu")
	except Exception as exception:
		print (exception)
#2
def addClient(bank_name, client_name, client_money):
	global allBanks
	if isinstance(client_name,str):
		try:
			if client_name not in allBanks[bank_name]:
				if isinstance(client_money, str):
					client_money = float(client_money)
				if client_money < 0:
					client_money = 0
				allBanks[bank_name][client_name] = {"money": client_money}

			else:
				raise Exception("This client is already exist!")
		except ValueError:
			print("Money: Must be a number!")
		except Exception as exception:
			print(exception)

	else:
		raise TypeError(client_name+" : it is not a name!")


#3
def transfer(bank_name, client1, client2, money):
	global allBanks
	if client1 in allBanks[bank_name] and client2 in allBanks[bank_name]:
		try:
			if isinstance(money, str):
				money = float(money)
			allBanks[bank_name][client1]['money'] -= money
			allBanks[bank_name][client2]['money'] += money
		except ValueError:
			print("Money: Must be a number!")
	else:
		print("Wrong client name!")

#4
def addMoneyToClient(bank_name, client, money):
	global allBanks
	if client in allBanks[bank_name]:
		try:
			if isinstance(money, str):
				money = float(money)
			allBanks[bank_name][client]['money'] += money
		except ValueError:
			print("Money: Must be a number!")

	else:
		print("Wrong client name!")

#5
def showAllBanks():
	global allBanks
	print("№","Name")
	for i, bank in enumerate(allBanks,1):
		print(i,bank.title())

#6
def showAllClients(bank_name):
	global allBanks
	print("№","Name","Money")
	for i, client in enumerate(allBanks[bank_name],1):
		print(i,client.title(), allBanks[bank_name][client]['money'])

#7
def saveToFile(file_name):
	global allBanks
	with open(file_name,'w') as json_f:
		json.dump(allBanks, json_f)
		json_f.close()

#8
def readFromFile(file_name):
	global allBanks
	try:
		with open(file_name) as json_f:
			allBanks = json.load(json_f)
			json_f.close()
	except FileNotFoundError:
		print("No file")
		allBanks = {}

#9
def bankMenu(bank_name):
	while True:
		print("---\n"+bank_name)
		option = input("\n---\n1.Add a client\n2.Transfer\n3.Add money to client\n4.Back\n---\n")
		if option == "1":
			client_name = input("Client Name: ").lower()
			client_money = input("Money:")
			addClient(bank_name, client_name, client_money)
		elif option == "2":
			showAllClients(bank_name)
			client1 = input("From Client(Name): ").lower()
			client2 = input("To Client(Name): ").lower()
			money_transfer = input("Money: ")
			transfer(bank_name, client1, client2, money_transfer)
		elif option == "3":
			showAllClients(bank_name)
			client = input("Client name: ").lower()
			money_add = input("Money: ")
			addMoneyToClient(bank_name, client, money_add)
		elif option == "4":
			break


#####################################

if __name__=="__main__":
	readFromFile("Banks.txt")
	#global allBanks
	while True:
		option = input("---\n1.Create a bank\n2.Open a bank\n3.Save\n4.Quit\n---\n")
		if option == "1":
			bank_name = input("Bank name: ").lower()
			addBank(bank_name)
			bankMenu(bank_name)
		elif option == "2":
			showAllBanks()
			choosen_bank = input("Choose a bank( Write the bank name): ").lower()
			if choosen_bank in allBanks:
				bankMenu(choosen_bank)
		elif option == "3":
			saveToFile("Banks.txt")
		elif option == "4":
			break
