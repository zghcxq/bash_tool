


def addtool(tl):
	employee_file = open('config/tools.json','r')
   
	solvethesign = len(employee_file.read())

	employee_file.close()
	if solvethesign == 0:

		employee_file = open('config/tools.json','w') 
    
		employee_file.write(tl)
		employee_file.close()
	else:
	    
		employee_file = open('config/tools.json','a')
		solveutf8 ="//"+tl
		employee_file.write(solveutf8)
		employee_file.close()
 










	






