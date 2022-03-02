
import time
import requests
import webbrowser
from post import * 

while True : 

    response_paris = requests.post('https://trouverunlogement.lescrous.fr/api/fr/search/21', headers=headers_paris, cookies=cookies_paris, json=json_data_paris)
    total = response_paris.json()["results"]["total"]
    jprint(total)

    if total > 0 : 
        
        ## b = "https://trouverunlogement.lescrous.fr/tools/flow/21/search?bounds=-0.6387_44.9162_-0.5337_44.8108&page=1&price=60000"
        url = "https://trouverunlogement.lescrous.fr/tools/flow/21/search?bounds=2.2163_48.9716_2.4781_48.7458&page=1&price=60000"

        webbrowser.open(url, new= 0, autoraise=True)

    time.sleep(300)


