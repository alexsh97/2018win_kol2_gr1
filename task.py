#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Good Luck

from bank import bankc

choose = input("1.Create a bank;\n2.Choose a bank;\n")

if choose == "1":
	print("Creating a bank")
	bank_name = input("Bank name: ")
	new_bank = bankc(bank_name)
	mission = input("What next?\n 1.Add client\n2.List of clients\n3.Add money to client\n4.Transfer")
	if mission == 1:
		new_bank.addClient("Somebody","12345",60)
	if mission == 2:
		new_bank.listOfClient()	


