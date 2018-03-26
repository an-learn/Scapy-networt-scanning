#!/usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from datetime import datetime
from scapy.all import *

import threading
from Queue import Queue
q = Queue()

import sys
sys.path.append("..")
import main

def list_select():
	print"===========================\n"
	print"1.Enter IP address"
	print"  1.1 Normal"
	print"  1.2 Neatly (when IP too much,a little slow)\n"
	print"2.Select a file\n"

def list_ips():
	print"===========================\n"
	print"Separate IP address by \",\" (support \"1-254\")\n"

def list_iptxt():
	print"===========================\n"
	print"Select a file(.txt) with IP list\n"

def select():
	answer3 = raw_input("[discovery-ACK] Select > ")
	if answer3 == "1.1":
		list_ips()
		ips1()
	elif answer3 == "1.2":
		list_ips()
		ips2()
	elif answer3 == "2":
		list_iptxt()
		iptxt_start()
	elif answer3 == "show":
		list_select()
		select()
	elif answer3 == "bk":
		print"===========================\n"
		main.select_discovery()
	elif answer3 == "exit":
		sys.exit()
	else:
		print"===========================\n"
		print"No Such Number,Select again.\n"
		select()

#############################################
############### 1.1 Normal ##################
#############################################

def ips1():
	global ips_list_h,ips_list_c
	ips_list_h = []			# "-" hyphen
	ips_list_c = []			# "," comma
	ips_input = raw_input("[discovery-ACK] IP > ")
	if ips_input == "bk":
		print"===========================\n"
		select()
	elif ips_input == "exit":
		sys.exit()
	else:
		ips_list = ips_input.split(',')
		ips_list_unre = list(set(ips_list))		#qu chong fu
		for i in ips_list_unre:
			if re.match(r"^(?:(?:1[0-9][0-9]\.)|(?:2[0-4][0-9]\.)|(?:25[0-5]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}(?:(?:1[0-9][0-9]\-)|(?:2[0-4][0-9]\-)|(?:25[0-5]\-)|(?:[1-9][0-9]\-)|(?:[0-9]\-))(?:(?:1[0-9][0-9])|(?:2[0-4][0-9])|(?:25[0-5])|(?:[1-9][0-9])|(?:[0-9]))$", i):
				ips_list_h.append(i)
			elif re.match(r"^(?:(?:1[0-9][0-9]\.)|(?:2[0-4][0-9]\.)|(?:25[0-5]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}(?:(?:1[0-9][0-9])|(?:2[0-4][0-9])|(?:25[0-5])|(?:[1-9][0-9])|(?:[0-9]))$", i):
				ips_list_c.append(i)
			else:
				print"===========================\n"
				print("Include incorrect IP format: "+i)
				print"Try again\n"
				ips1()
		t1 = datetime.now()
		print"===========================\n"
		ips1_h_start()
	print"finish in "+str(datetime.now()-t1)
	print"---------------------------"
	ips1()

#############################################

def ips1_h_start():
	global ips_list_h,ips_list_c
	ips_h_num = len(ips_list_h)
	for ih in range(0,ips_h_num):
		addr1 = int(ips_list_h[ih].split('.')[3].split('-')[0])
		addr2 = int(ips_list_h[ih].split('.')[3].split('-')[1])
		prefix = ips_list_h[ih].split('.')[0] + '.' + ips_list_h[ih].split('.')[1] + '.' + ips_list_h[ih].split('.')[2] + '.'
		for addr in range(addr1,addr2+1):
			iph = prefix + str(addr)
			ips_list_c.append(iph)	
	ips1_c_start()
	
#############################################

def ips1_c_start():
	global ips_list_c
	ips_list_c = list(set(ips_list_c))
	ips_c_num = len(ips_list_c)
	print" Alive:"
	map(q.put,xrange(0,ips_c_num))
	threads = [threading.Thread(target=worker1_c) for i in xrange(50)]
	map(lambda x:x.start(),threads)
	q.join()

def ips1_c(ic):
	answer1 = sr1(IP(dst = ips_list_c[ic])/TCP(dport=80,flags="A"),timeout=1,verbose=0)
	answer2 = sr1(IP(dst = ips_list_c[ic])/TCP(dport=445,flags="A"),timeout=1,verbose=0)
	answer3 = sr1(IP(dst = ips_list_c[ic])/TCP(dport=2222,flags="A"),timeout=1,verbose=0)
	if answer1 == None and answer2 == None and answer3 == None:
		pass
	else:
		print(ips_list_c[ic]+"\n")

def worker1_c():
	while not q.empty():
		ic = q.get()
		try:
			ips1_c(ic)
		finally:
			q.task_done()

#############################################
############## 1.2 Neatly ###################
#############################################

def ips2():
	global ips_list_h,ips_list_c,ips_c_num,ips_h_num
	ips_list_h = []			# "-" hyphen
	ips_list_c = []			# "," comma
	ips_input = raw_input("[discovery-ACK] IP > ")
	if ips_input == "bk":
		print"===========================\n"
		select()
	elif ips_input == "exit":
		sys.exit()
	else:
		ips_list = ips_input.split(',')
		ips_list_unre = list(set(ips_list))		#qu chong fu
		for i in ips_list_unre:
			if re.match(r"^(?:(?:1[0-9][0-9]\.)|(?:2[0-4][0-9]\.)|(?:25[0-5]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}(?:(?:1[0-9][0-9]\-)|(?:2[0-4][0-9]\-)|(?:25[0-5]\-)|(?:[1-9][0-9]\-)|(?:[0-9]\-))(?:(?:1[0-9][0-9])|(?:2[0-4][0-9])|(?:25[0-5])|(?:[1-9][0-9])|(?:[0-9]))$",i):
				ips_list_h.append(i)
			elif re.match(r"^(?:(?:1[0-9][0-9]\.)|(?:2[0-4][0-9]\.)|(?:25[0-5]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}(?:(?:1[0-9][0-9])|(?:2[0-4][0-9])|(?:25[0-5])|(?:[1-9][0-9])|(?:[0-9]))$",i):
				ips_list_c.append(i)
			else:
				print"===========================\n"
				print("Include incorrect IP format: "+i)
				print"Try again\n"
				ips2()
		t1 = datetime.now()
		print"===========================\n"
		ips_c_num = len(ips_list_c)
		ips_h_num = len(ips_list_h)
		if ips_c_num > 0:
			print("Divide all IP into "+str(len(ips_list_h)+1)+" lists:\n")
			ips2_c_start()
			ips2_h_start()
		else:
			print("Divide all IP into "+str(len(ips_list_h))+" lists:\n")
			ips2_h_start()
	print"\nfinish in "+str(datetime.now()-t1)
	print"---------------------------"
	ips2()

		
#############################################

def ips2_c_start():
	print"---------------------------"
	print(" "+str(ips_c_num)+" IP in:\n"+str(ips_list_c)+"\n\n Alive:")
	
	map(q.put,xrange(0,ips_c_num))
	threads = [threading.Thread(target=worker2_c) for i in xrange(50)]
	map(lambda x:x.start(),threads)
	q.join()

def ips2_c(ic):
	answer1 = sr1(IP(dst = ips_list_c[ic])/TCP(dport=80,flags="A"),timeout=1,verbose=0)
	answer2 = sr1(IP(dst = ips_list_c[ic])/TCP(dport=445,flags="A"),timeout=1,verbose=0)
	answer3 = sr1(IP(dst = ips_list_c[ic])/TCP(dport=2222,flags="A"),timeout=1,verbose=0)
	if answer1 == None and answer2 == None and answer3 == None:
		pass
	else:
		print(ips_list_c[ic]+"\n")

def worker2_c():
	while not q.empty():
		ic = q.get()
		try:
			ips2_c(ic)
		finally:
			q.task_done()

#############################################

def ips2_h_start():
	global prefix
	for ih in range(0,ips_h_num):
		addr1 = int(ips_list_h[ih].split('.')[3].split('-')[0])
		addr2 = int(ips_list_h[ih].split('.')[3].split('-')[1])
		prefix = ips_list_h[ih].split('.')[0] + '.' + ips_list_h[ih].split('.')[1] + '.' + ips_list_h[ih].split('.')[2] + '.'
		print"---------------------------"
		print(str(addr2 - addr1 + 1)+" IP in:\n['"+str(ips_list_h[ih])+"']\n\n Alive:")
		
		map(q.put,xrange(addr1,addr2+1))
		threads = [threading.Thread(target=worker2_h) for i in xrange(50)]
		map(lambda x:x.start(),threads)
		q.join()

def ips2_h(addr):
	answer1 = sr1(IP(dst = prefix + str(addr))/TCP(dport=80,flags="A"),timeout=1,verbose=0)
	answer2 = sr1(IP(dst = prefix + str(addr))/TCP(dport=445,flags="A"),timeout=1,verbose=0)
	answer3 = sr1(IP(dst = prefix + str(addr))/TCP(dport=2222,flags="A"),timeout=1,verbose=0)
	if answer1 == None and answer2 == None and answer3 == None:
		pass
	else:
		print(prefix+str(addr)+"\n")

def worker2_h():
	while not q.empty():
		addr = q.get()
		try:
			ips2_h(addr)
		finally:
			q.task_done()

#############################################
############# 2.Select a file ###############
#############################################

def iptxt_start():
	filename = raw_input("[discovery-ACK] Filename > ")
	if filename == "bk":
		print"===========================\n"
		select()
	elif filename == "exit":
		sys.exit()
	else:
		t1 = datetime.now()
		try:
			file = open(filename,'r')
			print"===========================\n"
			print" Alive:"
			map(q.put,file)
			threads = [threading.Thread(target=worker_iptxt) for i in xrange(50)]
			map(lambda x:x.start(),threads)
			q.join()
		except IOError:
			print"==========================="
			print"File \""+filename + "\" not exist"
			print"Try again\n"
	print"finish in "+str(datetime.now()-t1)
	print"---------------------------"
	iptxt_start()
	

def iptxt(ipt):
	answer1 = sr1(IP(dst=ipt.strip())/TCP(dport=80,flags="A"),timeout=1,verbose=0)
	answer2 = sr1(IP(dst=ipt.strip())/TCP(dport=445,flags="A"),timeout=1,verbose=0)
	answer3 = sr1(IP(dst=ipt.strip())/TCP(dport=24242,flags="A"),timeout=1,verbose=0)
	if answer1 == None and answer2 == None and answer3 == None:
		pass
	else:
		print(ipt.strip()+"\n")

def worker_iptxt():
	while not q.empty():
		ipt = q.get()
		try:
			iptxt(ipt)
		finally:
			q.task_done()

#############################################

def tcpack_ping_start():
	list_select()
	select()

if __name__ == '__main__':
	tcpack_ping_start()
