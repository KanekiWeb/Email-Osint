import colorama, requests, ScrapeSearchEngine
from ScrapeSearchEngine.SearchEngine import *
from colorama import Fore

def pastebin_check(i, email):
	try:
		link = str(i).replace("https://pastebin.com/","https://pastebin.com/raw/")
		r = requests.get(link)
		data = r.text

		if email.lower() in data.lower() or email in data:
			print(Fore.GREEN+"> "+link)

	except:
		print("[!] Your adresse IP has banned, retry tomorrow or change your ip.".replace('!',Fore.RED+'!'+Fore.RESET))

def pastebin_dump(email):
	search = ("site:pastebin.com \"{}\"".format(email))
	try:
		googleText, googleLink = Google(search=search, userAgent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Safari/537.36")
		googleLinks = googleText
		
		for i in googleLink:
			pastebin_check(i, email)

	except:
		print("[!] Error or no pastebin link Found.".replace('!',Fore.RED+'!'+Fore.RESET))