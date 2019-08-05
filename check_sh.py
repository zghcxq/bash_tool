import os

def checksh(num):
	employee_file = open('config/tools.json','r')
	solvethesign = len(employee_file.read())
	employee_file.close()
	if solvethesign == 0:
		print("null")
	else:
		employee_file = open('config/tools.json','r')
		for employee in employee_file.readlines():
			spilted = employee.split('//')
		employee_file.close()
		num= int(num)
		sh_tool_Name=spilted[num-1]+".sh"
		os.system("sudo gedit tools_sh/"+sh_tool_Name)








	






