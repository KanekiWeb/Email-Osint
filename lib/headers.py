import colorama, os
from colorama import Fore

def Header(text):
	os.system('title Email Osint ^| '+text)
	print("")
	print("-------------------------------")
	print(f"{Fore.GREEN}>{Fore.RESET}  "+text)
	print("-------------------------------")