import json 
import requests
from bs4 import BeautifulSoup

URL = "https://trouverunlogement.lescrous.fr/tools/flow/21/search?bounds=2.2241_48.9022_2.4698_48.8156&page=1&price=60000"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

mydivs = soup.find_all("div", {"class": "app"})

# print(soup.prettify())
# print(mydivs)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

query = requests.get("https://trouverunlogement.lescrous.fr/photon/api?q=%27paris%27")

x = soup.select('meta[id="app-initialState"]')
print(x[0].attrs["content"])

# jprint(query.json())


