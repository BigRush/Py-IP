#!/usr/bin/env python3.7

################################################################################
# Author :	BigRush
#
# License :  GPLv3
#
# Description :  Shows internal and external IP address
#
# Version :  1.0.0
################################################################################


import os
import socket
import ifaddr

def Internal_IP():
	try:
		int_ip = socket.gethostbyname(socket.gethostname())
		print("Your internal IP is: {}".format(int_ip))
	
	except:
		print("Can't retrieve internal IP")
		

def External_IP():
	inter = ifaddr.get_adapters()
	for i in inter:
            for j in i.ips:
                #print(filter)
                #print(type(filter))
                pre_filter = "{}: {}".format(i.nice_name, j.ip)
                filter += "{}\n".format(pre_filter)

        print(filter)
        result = re.match(r'enp*', filter)
        print(result.group(0))



