import colorama, os, argparse
from colorama import Fore

from lib.headers import Header

from modules.emailrep import emailrep
from modules.verify_email import verify_email
from modules.BreachedSites import BreachedSites

parser = argparse.ArgumentParser()
parser.add_argument('-e','--email',help="Email Adresse")
args = parser.parse_args()

email = (args.email)

os.system('cls')
print(f'\n			 Author : {Fore.BLUE}Kaneki{Fore.RESET} | Github : {Fore.BLUE}github.com/KanekiX2{Fore.RESET} | Discord : {Fore.BLUE}discord.gg/vGKQs4Cczy{Fore.RESET}')

# Email Réputation
Header(text="Email Réputation")
emailrep(email=email)

# Email Vérification
Header(text="Email Vérification")
verify_email(email=email)

# Breached Leaks Website
Header(text="Breached Leaks Website")
BreachedSites(email=email)