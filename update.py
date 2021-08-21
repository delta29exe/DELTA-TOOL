#!/usr/bin/env python3

import os
os.system("clear")
os.system("figlet R.H.A-TOOL")
print("RED HACK TEAM AZE - R.H.A")
print("""Guncellemeni Baslatmaq ucun [Y] yazib
Enter-e Basin""")
alqoritm=input("R.H.A-TOOL = UPDATE : ")
if alqoritm=="exit":
	print("Helelik")
	quit()
elif alqoritm=="Y" or alqoritm=="y":
	os.system("cowsay R.H.A-TOOL GUNCELLENIR")
	os.system("git clone https://github.com/delta29exe/R.H.A-TOOL")
	os.system("figlet RED HACK AZE")
	os.system("cowsay R.H.A-TOOL GUNCELLENMISDIR")
	secim=input("Cixmaq Ucun C yazib Enter-e basin : ")
	if secim=="C" or secim=="c":
		os.system("exit")
elif alqoritm=="nano" or alqoritm=="nano update.py":
	os.system("exit")
	os.system("nano update.py")
else:
	print("Secim-i Duzgun Yazin. Cixilir...")
	quit()

