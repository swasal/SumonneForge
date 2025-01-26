import requests
import core.assets.riot.datadragon as datadragon

url=f"https://ddragon.leagueoflegends.com/cdn/{datadragon.version}/data/en_US/champion/Ahri.json"
rawdata=requests.get(url).json()['data']
x=rawdata['Ahri']['image']


for k,v in x.items():
    print(f"{k} : {v}")

print("======\n\n\n")
