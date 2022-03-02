import json
import time
import webbrowser
import requests

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


cookies_paris = {
    '_pk_ref.1.5ea2': '%5B%22%22%2C%22%22%2C1646234498%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.1.5ea2': 'c3b829e1348d5a81.1644758647.',
    'qpid': 'c8fon0al6fqieh0id080',
    'SimpleSAMLSessionID': '7f96ba8d789db2bc1dfa4f2807e41051',
    'HAPROXYID': 'app4',
    '_pk_ses.1.5ea2': '1',
}

headers_paris = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Accept': 'application/ld+json, application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://trouverunlogement.lescrous.fr/tools/flow/21/search?bounds=2.1607_48.9034_2.5322_48.8141&page=1&price=60000&residence=3c78574c-0b58-11e8-89ed-005056940822',
    'Origin': 'https://trouverunlogement.lescrous.fr',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

json_data_paris = {
    'precision': 6,
    'need_aggregation': True,
    'page': 1,
    'pageSize': 24,
    'sector': None,
    'idTool': 21,
    'occupationModes': [],
    'residence': '3c78574c-0b58-11e8-89ed-005056940822',
    'equipment': [],
    'price': {
        'min': 0,
        'max': None,
    },
    'location': [
        {
            'lon': 2.2241,
            'lat': 48.9022,
        },
        {
            'lon': 2.4698,
            'lat': 48.8156,
        },
    ],
}

while True : 

    response_paris = requests.post('https://trouverunlogement.lescrous.fr/api/fr/search/21', headers=headers_paris, cookies=cookies_paris, json=json_data_paris)
    total = response_paris.json()["results"]["total"]
    jprint(total)

    if total > 0 : 
        
        url = "https://trouverunlogement.lescrous.fr/tools/flow/21/search?bounds=2.2241_48.9022_2.4698_48.8156&page=1&price=60000&residence=3c78574c-0b58-11e8-89ed-005056940822"

        webbrowser.open(url, new=0, autoraise=True)

    time.sleep(600)



    









#########################


cookies = {
    '_pk_ref.1.5ea2': '%5B%22%22%2C%22%22%2C1646230505%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.1.5ea2': 'c3b829e1348d5a81.1644758647.',
    'qpid': 'c8fnuiql6fqieh0ibqig',
    'SimpleSAMLSessionID': '7f96ba8d789db2bc1dfa4f2807e41051',
    'HAPROXYID': 'app4',
    '_pk_ses.1.5ea2': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Accept': 'application/ld+json, application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://trouverunlogement.lescrous.fr/tools/flow/21/search?bounds=-0.7088_44.924_-0.4637_44.803&page=1&price=60000',
    'Origin': 'https://trouverunlogement.lescrous.fr',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

json_data = {
    'precision': 6,
    'need_aggregation': True,
    'page': 1,
    'pageSize': 24,
    'sector': None,
    'idTool': 21,
    'occupationModes': [],
    'equipment': [],
    'price': {
        'min': 0,
        'max': None,
    },
    'location': [
        {
            'lon': -0.6387,
            'lat': 44.9162,
        },
        {
            'lon': -0.5337,
            'lat': 44.8108,
        },
    ],
}

# response = requests.post('https://trouverunlogement.lescrous.fr/api/fr/search/21', headers=headers, cookies=cookies, json=json_data)
# jprint(response.json()["results"]["total"])

# while True : 

#     response = requests.post('https://trouverunlogement.lescrous.fr/api/fr/search/21', headers=headers, cookies=cookies, json=json_data)
#     total = response.json()["results"]["total"]
#     jprint(total)

#     if total >= 0 : 
        
#         url = "https://trouverunlogement.lescrous.fr/tools/flow/21/search?bounds=2.2241_48.9022_2.4698_48.8156&page=1&price=60000&residence=3c78574c-0b58-11e8-89ed-005056940822"

#         webbrowser.open(url, new=0, autoraise=True)

#     time.sleep(5)