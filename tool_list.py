def listoftools():
		employee_file = open("config/tools.json", "r") 
		solvethesign = len(employee_file.read())

		employee_file.close()
		
		if solvethesign == 0:
			print("null")
		else:
			employee_file = open("config/tools.json", "r") 	
			for employee in employee_file.readlines():
				spilted = employee.split('//')  
			print ("-----------------------------")
			print ("|     toolslist             |")
			i=0
			for ipaddresschoose in range(0,len(spilted)):
				i = i+1
				solverange = ipaddresschoose
				ipaddress = spilted[solverange]
				print ("-----------------------------")
				print ("* "+str(i)+ ". "+ipaddress + "        ")
	
			print ("-----------------------------")    
			employee_file.close()
