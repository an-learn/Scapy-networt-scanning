#!/usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#import subprocess
from datetime import datetime
from scapy.all import *

import threading
from Queue import Queue

import sys
sys.path.append("..")
import main

#############################################

interfaces = subprocess.check_output("ifconfig | grep ': ' | cut -d ':' -f1",shell=True).strip()
number_interfaces = subprocess.check_output("ifconfig | grep ': ' | awk 'END{print NR}'",shell=True).strip()
q = Queue()

#############################################

def arp_ping_prepare():
	print"===========================\n"
	print("Select one from this "+number_interfaces+" interface:\n\n"+interfaces+"\n")

	interface = raw_input("[arp ping] Select > ")
	if interface == "bk":
		print"===========================\n"
		main.select_discovery()
	elif interface == "exit":
		sys.exit()
	else:
		global ip,prefix
		ip = subprocess.check_output("ifconfig "+interface+" | grep 'netmask' | cut -d' ' -f10 | cut -d'.' -f1-3",shell=True).strip()
		prefix = ip.split('.')[0]+'.'+ip.split('.')[1]+'.'+ip.split('.')[2]+'.'
		
		print("===========================\n")
		print"These IP are alive:\n"

def arp_ping_start():
	arp_ping_prepare()
	t1 = datetime.now()
	map(q.put,xrange(1,254))
	threads = [threading.Thread(target=worker) for i in xrange(50)]
	map(lambda x:x.start(),threads)
	q.join()
	print"finish in "+str(datetime.now()-t1)
	print"---------------------------"
	main.select_discovery()

def arp_ping(addr):
		answer = sr1(ARP(pdst=prefix+str(addr)),timeout=1,verbose=0)
		if answer == None:
			pass
		else:
			print(prefix+str(addr)+"\n")

def worker():
	while not q.empty():	
		addr = q.get()
		try:
			arp_ping(addr)
		finally:
			q.task_done()

if __name__ == '__main__':
	arp_ping_start()

