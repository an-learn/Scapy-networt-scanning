#!/usr/bin/python

import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#import subprocess
from scapy.all import *

import discovery.arp_ping
import discovery.ping
import discovery.tcpsyn_ping
import discovery.tcpack_ping
import discovery.tcpsa_ping
import discovery.udp_ping
import discovery.oba_ping
import scanning.udp_port
import scanning.tcpsyn_port
import scanning.tcpconnect_port
import scanning.tcpnull_port
import scanning.tcpfin_port
import scanning.tcpxmas_port
import scanning.tcpack_port
import scanning.tcpwindow_port
import scanning.tcpmaimon_port
import scanning.tcpzombie_port
import scanning.tcpdiy_port
import firewall.firewall_tcp
import fingerprinter.banner_tcp

#############################################


#############################################

def title():
	print"################################"
	print"#                              #"
	print"#    Scapy Network Scanning    #"
	print"#            V1.0              #"
	print"#         by Anlearn           #"
	print"#                              #"
	print"################################\n\n"""

def list_main():
	print"Select An Option from the Menu:\n"
	print"1.Discovery Scanning\n"
	print"2.Port Scanning\n"
	print"3.Firewall Scanning\n"
	print"4.Fingerprinting\n"
	print"5.More\n"

def list_more():
	print"===========================\n"
	print"This is the first tool I have writen,and it is not maturity\n"
	print"I hope maybe you would like to help me enhance.\n"
	print"It will more finaldetails with the help of you."
	print"Welcome to join,my friend !\n"
	select_main()

def list_discovery():
	print"===========================\n"
	print"Choose a type of Discovery Scanning:\n\n"
	print"------ layer 2 ------\n"
	print"1.ARP Ping\n"
	print"------ layer 3 ------\n"
	print"2.Ping\n"
	print"------ layer 4 ------\n"
	print"3.TCP SYN Ping\n"
	print"4.TCP ACK Ping\n"
	print"5.TCP SYN+ACK Ping\n"
	print"6.UDP Ping\n"
	print"------- other -------\n"
	print"7.All but ARP Ping\n"

def list_port():
	print"===========================\n"
	print"Choose a type of Port Scanning:\n\n"
	print"1.UDP scanning\n"
	print"2.TCP SYN scanning\n"
	print"3.TCP Connect scanning\n"
	print"------ stealth ------\n"
	print"4.TCP Null scanning\n"
	print"5.TCP FIN scanning\n"
	print"6.TCP FIN+PSH+URG(xmas) scanning\n"
	print"------ unusual ------\n"
	print"7.TCP ACK scanning\n"
	print"8.TCP Window scanning\n"
	print"9.TCP FIN+ACK(maimon) scanning\n"
	print"10.TCP Zombie scanning\n"
	print"11.TCP Diy flags scanning\n"

def list_firewall():
	print"===========================\n"
	print"Choose a type of Firewall Scanning:\n\n"
	print"1.Firewall for TCP\n"
	
def list_fingerprinting():
	print"===========================\n"
	print"Choose a type of Fingerprinting Scanning:\n\n"
	print"1.Banner scanning\n"

#############################################

def select_discovery():
	answer2 = raw_input("[discovery] Select > ")
	if answer2 == "1":
		discovery.arp_ping.arp_ping_start()
	elif answer2 == "2":
		discovery.ping.ping_start()
	elif answer2 == "3":
		discovery.tcpsyn_ping.tcpsyn_ping_start()
	elif answer2 == "4":
		discovery.tcpack_ping.tcpack_ping_start()
	elif answer2 == "5":
		discovery.tcpsa_ping.tcpsa_ping_start()
	elif answer2 == "6":
		discovery.udp_ping.udp_ping_start()
	elif answer2 == "7":
		discovery.oba_ping.oba_ping_start()
	elif answer2 == "show":
		list_discovery()
		select_discovery()
	elif answer2 == "bk":
		print"==========================="
		select_main()
	elif answer2 == "exit":
		sys.exit()
	else:
		print"===========================\n"
		print"No Such Number,Select again.\n"
		select_discovery()

def select_port():
	answer2 = raw_input("[port] Select > ")
	if answer2 == "1":
		scanning.udp_port.udp_port_start()
	elif answer2 == "2":
		scanning.tcpsyn_port.tcpsyn_port_start()
	elif answer2 == "3":
		scanning.tcpconnect_port.tcpconnect_port_start()
	elif answer2 == "4":
		scanning.tcpnull_port.tcpnull_port_start()
	elif answer2 == "5":
		scanning.tcpfin_port.tcpfin_port_start()
	elif answer2 == "6":
		scanning.tcpxmas_port.tcpxmas_port_start()
	elif answer2 == "7":
		scanning.tcpack_port.tcpack_port_start()
	elif answer2 == "8":
		scanning.tcpwindow_port.tcpwindow_port_start()
	elif answer2 == "9":
		scanning.tcpmaimon_port.tcpmaimon_port_start()
	elif answer2 == "10":
		scanning.tcpzombie_port.tcpzombie_port_start()
	elif answer2 == "11":
		scanning.tcpdiy_port.tcpdiy_port_start()
	elif answer2 == "show":
		list_port()
		select_port()
	elif answer2 == "bk":
		print"==========================="
		select_main()
	elif answer2 == "exit":
		sys.exit()
	else:
		print"===========================\n"
		print"No Such Number,Select again.\n"
		select_port()

def select_firewall():
	answer2 = raw_input("[firewall] Select > ")
	if answer2 == "1":
		firewall.firewall_tcp.firewall_tcp_start()
	elif answer2 == "show":
		list_firewall()
		select_firewall()
	elif answer2 == "bk":
		print"==========================="
		select_main()
	elif answer2 == "exit":
		sys.exit()
	else:
		print"===========================\n"
		print"No Such Number,Select again.\n"
		select_firewall()

def select_fingerprinting():
	answer2 = raw_input("[fingerprint] Select > ")
	if answer2 == "1":
		fingerprinter.banner_tcp.banner_tcp_start()
	elif answer2 == "show":
		list_fingerprinting()
		select_fingerprinting()
	elif answer2 == "bk":
		print"==========================="
		select_main()
	elif answer2 == "exit":
		sys.exit()
	else:
		print"===========================\n"
		print"No Such Number,Select again.\n"
		select_fingerprinting()

def select_main():
	answer1 = raw_input("[main] Select > ")
	if answer1 == "1":
		list_discovery()
		select_discovery()
	elif answer1 == "2":
		list_port()
		select_port()
	elif answer1 == "3":
		list_firewall()
		select_firewall()
	elif answer1 == "4":
		list_fingerprinting()
		select_fingerprinting()
	elif answer1 == "5":
		list_more()
	elif answer1 == "show":
		print"===========================\n"
		list_main()
		select_main()
	elif answer1 == "exit":
		sys.exit()
	else:
		print"===========================\n"
		print"No Such Number,Select again.\n"
		select_main()

#############################################


if __name__ == '__main__':
	title()
	list_main()
	select_main()
