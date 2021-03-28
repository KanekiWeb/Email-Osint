import colorama, os, argparse
from colorama import Fore

from lib.headers import Header

from modules.emailrep import emailrep
from modules.verify_email import verify_email
from modules.BreachedSites import BreachedSites
from modules.PastebinDump import pastebin_dump
from modules.Holehe_Module import account_detect
from modules.leakcheck import api_leakcheck

parser = argparse.ArgumentParser()
parser.add_argument('-e','--email',help="Email Adresse")
args = parser.parse_args()

email = (args.email)

print(f'\n			 Author : {Fore.CYAN}Kaneki{Fore.RESET} | Github : {Fore.CYAN}github.com/KanekiX2{Fore.RESET} | Discord : {Fore.CYAN}discord.gg/vGKQs4Cczy{Fore.RESET}')

# Email Réputation
Header(text="Email Réputation")
emailrep(email=email)

# Email Vérification
Header(text="Email Vérification")
verify_email(email=email)

# Dump pastebin
Header(text="Dump pastebin")
pastebin_dump(email=email)

# Breached Leaks Website
Header(text="Breached Leaks Website")
BreachedSites(email=email)

# Account Checking
Header(text="Account Detection")
account_detect(email=email)

# Search Data Breach
Header(text="Data Breach")
api_leakcheck(email=email)
