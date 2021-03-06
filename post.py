import json

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
