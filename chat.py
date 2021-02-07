import socket
import threading 
import os
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

os.system("tput setaf 11")
ip = input("\n\t\tEnter Your IP : ")
port = 1234

s.bind( (ip,port) )

sip = input("\n\t\tEnter Server IP : ")
sport = 1234

print()
os.system('clear')
os.system('tput setaf 222')
os.system('figlet UdP cHaT aPp')

def send():

    while True:
        os.system('tput setaf 46')
        msg = input('\n').encode()
        s.sendto(msg,(sip,sport))
        if msg.decode() == "exit":
            os.system('tput setaf 7')
            os._exit(1)
        
def recv():
    while True:
        os.system('tput setaf 51')
        print('')
        msg = s.recvfrom(1024)
        if msg[0].decode() == "exit":
            os._exit(1) 
        print('\n\t\t\t\t :^=^: ' + msg[0].decode())
    



t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recv)

t1.start()
t2.start()
