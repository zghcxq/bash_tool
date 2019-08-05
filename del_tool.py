
import os

def deltool(num):
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
		employee_file = open('config/tools.json','w')

		num= int(num)
		
		bash_name=spilted[num-1]+".sh"
		os.system("rm -rf tools_sh/"+bash_name)
		spilted[num-1]=''

		if num ==1 :
			toolsstr=""
			toolsstr =toolsstr+spilted[1]
			for length in range(2,len(spilted)):
				toolsstr=toolsstr +"//"+spilted[length]
			employee_file.write(toolsstr)
			
		else:
			toolsstr=spilted[0]
			for length in range(1,len(spilted)):
				if len(spilted[length])==0:
					toolsstr=toolsstr +spilted[length]
				else:
					toolsstr=toolsstr +"//"+spilted[length]
			
			employee_file.write(toolsstr)
		employee_file.close()
 	

#ssr-linux-64//v2ray-linux-64//simplescreenrecorder//chrome//git//ss-qt//proxychains//chromium








	






