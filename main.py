import add_tool
import tool_list
import del_tool
import install_tool
import check_sh
import os
import sys


def help():
		print ("tools version 1.0.0  ( author:dawn)")
		print("usage: python3 main.py -h  [help]")
		print("usage: python3 main.py -a  [add  a tool]")
		print("usage: python3 main.py -l  [list of tools] | -r [remove] <number of tool>/ -i [install] <number of tool>/ -c [check] <number of tool>")
		


def main():

	if len(sys.argv)==1:	
		help()
	
	elif len(sys.argv)==2:
		if sys.argv[1] == "-h":
			help()
		if sys.argv[1] == "-a":
			s = input("please Enter toolName : ")
			add_tool.addtool(s)
			bash_name= s+".sh"
			os.system("touch tools_sh/"+bash_name)
			tool_sh_source= "tools_sh/"+bash_name
			employee_file = open(tool_sh_source,"w")
			data = []
			input_ch =''
			Ln=0
			print("please Enter "+bash_name+" code : ")
			while True:
				input_ch = input()
				Ln= Ln+1
				is_tools = input_ch.find(';')
				if (is_tools != -1):
					input_ch = input_ch.split(';')[0] 
					data.append(input_ch)					
					break
				else:
					data.append(input_ch+"\n")
			for lnnum in range(0,Ln):	
				employee_file.write(data[lnnum])
			employee_file.close()

		if sys.argv[1] == "-l":	
			tool_list.listoftools()
		
	elif len(sys.argv)==4:
		if sys.argv[1] == "-l":
			if sys.argv[2]=="-r":
				del_tool.deltool(sys.argv[3])
			if sys.argv[2]=="-i":
				install_tool.installtool(sys.argv[3])
			if sys.argv[2]=="-c":
				check_sh.checksh(sys.argv[3])
	
		
			

main()

