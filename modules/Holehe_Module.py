'''
HOLELE LICENSE -> https://www.gnu.org/licenses/gpl-3.0.fr.html

Twitter : @palenath
Github : https://github.com/megadose
Holehe : https://github.com/megadose/holehe
'''

import trio, httpx

from holehe.modules.shopping.amazon import *
from holehe.modules.shopping.ebay import *

from holehe.modules.transport.blablacar import *

from holehe.modules.crowfunding.buymeacoffee import *

from holehe.modules.forum.cracked_to import *

from holehe.modules.social_media.discord import *
from holehe.modules.social_media.instagram import *
from holehe.modules.social_media.twitter import *
from holehe.modules.social_media.snapchat import *

from holehe.modules.programing.github import *

from holehe.modules.transport.blablacar import *

from holehe.modules.music.spotify import *

from holehe.modules.porn.pornhub import *
from holehe.modules.porn.redtube import *
from holehe.modules.porn.xvideos import *

from holehe.modules.shopping.ebay import *
from holehe.modules.shopping.amazon import *

from holehe.modules.forum.cracked_to import *

def account_detect(email):
	try:
		list_acc = []
		async def acc_amazon():
		    out = []
		    client = httpx.AsyncClient()
		    await amazon(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_ebay():
		    out = []
		    client = httpx.AsyncClient()
		    await ebay(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_blablacar():
		    out = []
		    client = httpx.AsyncClient()
		    await blablacar(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_buymeacoffee():
		    out = []
		    client = httpx.AsyncClient()
		    await buymeacoffee(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_cracked_to():
		    out = []
		    client = httpx.AsyncClient()
		    await cracked_to(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_github():
		    out = []
		    client = httpx.AsyncClient()
		    await github(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_snapchat():
		    out = []
		    client = httpx.AsyncClient()
		    await snapchat(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_discord():
		    out = []
		    client = httpx.AsyncClient()
		    await discord(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_instagram():
		    out = []
		    client = httpx.AsyncClient()
		    await instagram(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_twitter():
		    out = []
		    client = httpx.AsyncClient()
		    await twitter(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_spotify():
		    out = []
		    client = httpx.AsyncClient()
		    await spotify(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_redutbe():
		    out = []
		    client = httpx.AsyncClient()
		    await redtube(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_pornhub():
		    out = []
		    client = httpx.AsyncClient()
		    await pornhub(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		async def acc_xvideos():
		    out = []
		    client = httpx.AsyncClient()
		    await xvideos(email, client, out)
		    list_acc.append(out)
		    await client.aclose()

		trio.run(acc_amazon)
		trio.run(acc_ebay)
		trio.run(acc_blablacar)
		trio.run(acc_buymeacoffee)
		trio.run(acc_cracked_to)
		trio.run(acc_github)
		trio.run(acc_snapchat)
		trio.run(acc_discord)
		trio.run(acc_instagram)
		trio.run(acc_twitter)
		trio.run(acc_spotify)
		trio.run(acc_redutbe)
		trio.run(acc_pornhub)
		trio.run(acc_xvideos)

		accounts_founds = []

		for i in list_acc:
		    try:
		        if i[0]['exists'] == True:
		            accounts_founds.append(i[0]['name'])
		    except:
		        pass

		a = accounts_founds
		founds = str(a).replace('[','').replace(']','').replace("'","").replace(', ','\n- ').upper()
		
		print("- "+founds)

	except:
		return None
