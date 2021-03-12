import requests, json, colorama
from colorama import Fore

def verify_email(email):
	try:
		r = requests.get('https://verify-email.org/home/verify-as-guest/test@gmail.com')
		data = r.json()
		status = data['response']['log']
		if status == "Succes":
			print("Email Status: OK".replace("OK",Fore.GREEN+"OK"+Fore.RESET))

		else:
			print("Email Status: FAIL".replace("FAIL",Fore.RED+"FAIL"+Fore.RESET))

	except:
		print("Verify-email.org API limit reached. Try again in 1 hour.")