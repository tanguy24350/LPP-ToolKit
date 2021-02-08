#!/bin/python3

#Importations des modules
import sys  # fonctions et paramètres systèmes
from datetime import datetime as dt
import random
import os #for clear function
import nmap
import ctypes
import subprocess

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\033[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033|92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033|8m'
    LOGGING = '\033[34m'


random_color =[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.LOGGING]
text_menu = '''
    ╔========================================================================================================╗
    ╟                                                                                                        ╟
    ╟                                                                                                        ╟
    ╟              PPPPPPP               PPPPPPPPPPP     PPPPPPPPPPP                                         ╟
    ╟              PLLLLLP               PLLLLLLLLLLP    PLLLLLLLLLLP                                        ╟
    ╟              PLLLLLP               PLLL     LLLP   PLLL     LLLP                                       ╟
    ╟              PLLLLLP               PLLL     LLLLP  PLLL     LLLLP                                      ╟
    ╟              PLLLLLP               PLLLLLLLLLLLP   PLLLLLLLLLLLP                                       ╟
    ╟              PLLLLLP               PLLLLLPPPPPP    PLLLLLPPPPPP                                        ╟
    ╟              PLLLLLP               PLLLLLP         PLLLLLP                                             ╟
    ╟              PLLLLLP               PLLLLLP         PLLLLLP                                             ╟
    ╟              PLLLLLP               PLLLLLP         PLLLLLP                                             ╟
    ╟              PLLLLLPPPPPPPPPPPPP   PLLLLLP         PLLLLLP                                             ╟
    ╟              PLLLLLLLLLLLLLLLLLP   PLLLLLP         PLLLLLP           .....   .....   .....             ╟
    ╟              PLLLLLLLLLLLLLLLLLP   PLLLLLP         PLLLLLP           .....   .....   .....             ╟
    ╟              PPPPPPPPPPPPPPPPPPP   PPPPPPP         PPPPPPP           .....   .....   .....             ╟
    ╟                                                                                                        ╟
    ╟                                                                                                        ╟
    ╟  ©LєƤтιтƤσυcєт                                                                                         ╟
    ╚========================================================================================================╝              '''



def sudo_access():
    if os.geteuid() != 0:
        print("You need to have root privileges to continue.")
        sys.exit(0)
         

def test1():
    scan=nmap.PortScanner()
    os.system('cls' if os.name == 'nt' else 'clear')
    ip=input("Enter IP:DNS : ")
    scan.scan(ip, "-p-", '-v -sS -sV -sC -A -O')
    scan.command_line()
    scan.scaninfo()
    for host in scan.all_hosts():
        print('.................................................................................................')
        print ('Host: %s(%s)' % (host, scan[host].hostname()))
        print ('State: %s' % scan[host].state())
        for proto in scan[host].all_protocols():
            print('........')
            print ('Protocol: %s' % proto)
            lport = scan[host][proto].keys()
            sorted(lport)
            for port in lport:
                print('port: %s\tstate: %s' % (port, scan[host][proto][port]['state']))



os.system('cls' if os.name == 'nt' else 'clear')
ch = True
while ch:
    random.shuffle(random_color)
    text_menu = text_menu + random_color[0]
    print(text_menu)
    print("""
        1. IP Full Analyze
        2. SQL Injections Tests
        3- Find hiddens URL's
        4- Leave Program
    """)
    selection=input("Select a choice : ")
    if selection=='1':
        sudo_access()
        test1()
    elif selection=='2':
        pass
        #options2
    elif selection=='3':
        pass
        #options3
    elif selection=='4':
        break
    else:        
        print("Unknown choice.")

