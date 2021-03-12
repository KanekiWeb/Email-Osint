import requests, json


def emailrep(email):
	r = requests.get('https://emailrep.io/{}'.format(email))
	data = r.text
	parsed = json.loads(data)

	try:
		disposable = parsed['details']['disposable']
		data_breach = parsed['details']['data_breach']
		spam = parsed['details']['spam']
		spoofable = parsed['details']['spoofable']

		if disposable == True:
		    disposable = (f"Email Disposable")

		if disposable == False:
		    disposable = (f"No Disposable Email")

		if data_breach == True:
		    data_breach = ("Leaks online found")

		if data_breach == False:
		    data_breach = ("No leaks found")

		if spam == True:
		    spam = (f"Spam reputation found")

		if spam == False:
		    spam = (f"No Spam reputation")

		if spoofable == True:
		    spoofable = (f"Spoofable")

		if spoofable == False:
		    spoofable = (f"No Spoofable")

		print("\nDisposable : "+disposable)
		print("Data Breach : "+data_breach)
		print("Spam reputation : "+spam)
		print("Spoofable : "+spoofable+"\n")

	except:
	    print("Emailrep.io API limit reached. Try again tomorrow.")