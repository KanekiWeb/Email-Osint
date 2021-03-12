import colorama, os
from colorama import Fore

def Header(text):
	os.system('title Email Osint ^| '+text)
	print("")
	prt1 = Fore.GREEN+"> "+Fore.RESET
	bs = "-" * len(text)
	print(prt1+text+":\n"+"---"+bs)