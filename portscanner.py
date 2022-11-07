#! /bin/python3

# This is a simple port scanner to find out the open ports in a given range
# This is inspired from the The Cyber Mentor youtube channel course - " Python for Beginners" 
# Course Link: https://www.youtube.com/watch?v=7utwZYKweho&t=5388s

import sys
import socket
from datetime import datetime as dt

#print('Port Scanner')

# Define your target

if len(sys.argv)==2:
	target=socket.gethostbyname(sys.argv[1]) # Translate hostname to IP address
else:
	print('Invalid number of arguments')
	print('Input format: python3 portscanner.py <ip_address>')

print("*"*50)
print(f"Scanning target: {target}")
print(f"Scan started at {str(dt.now())}")
print("*"*50)

try:
	s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	for port in range(79,85):
		#print(f"Scanning Port: {port}")
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port))
		if result==0:
			print(f"Port {port} is open")
		s.close()
	print("Scanning Complete")
except KeyboardInterrupt:
	print("Keyboard Interrupt, exiting program")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
except socket.error:
	print("Could not connect to the server")
	sys.exit()
	
		
