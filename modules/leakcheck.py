import leakcheck, terminaltables
from leakcheck import LeakCheckAPI
from terminaltables import SingleTable

'''
YOU CAN BUY API KEY HERE : https://leakcheck.net/

Plan basic : 2.99$ / day
Plan monthly : 9.99$ / month
Plan lifetime : 24.99$ / lifetime
Plan entreprise : 100$ / 3 month
'''

def api_leakcheck(email):
    keyy = "API KEY"
    api = LeakCheckAPI()
    try:
        api.set_key(keyy)
        api.set_type("email")
        api.set_query(email)
        result = api.lookup()[0:10] # 0:10 = Max of results, You can change for print more results
        
        TABLE_DATA = [
            ('Email & Pass', 'Leaked Name', 'Leaked Data')
        ]

        for i in result:
            try:
                password  = i['line']
            except:
                password = None
            try:
                leak_name1 = i['sources']
            except:
                leak_name1 = None
            try:
                leak_date = i['last_breach']
            except:
                leak_date = None

            leak_name = str(leak_name1).replace("'","").replace("[","").replace("]","")

            TABLE_DATA.append((password, leak_name, leak_date))

        table = SingleTable(TABLE_DATA)
        print(table.table)

    except:
        print("API key invalid or 0 attempts remaining !")
