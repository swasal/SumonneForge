"""Used to interact with riot's centralized database for league.
refer to => https://developer.riotgames.com/docs/lol#data-dragon

***NOTE***
This uses their online databse with the requests library.
"""

#imports
import requests

#checking for the latest datadragon version
url="https://ddragon.leagueoflegends.com/api/versions.json"
r=requests.get(url)
version= r.json()[0]

#functions
class profile:
    """Initializing the python"""
    def icon(id):
        "returns url to profile icon of the given id"
        url="http://ddragon.leagueoflegends.com/cdn/"+str(version)+"/img/profileicon/"+str(id)+".png"
        return url


class gameconstants:
    "gameconstants used by riot api from datadragon"
    def mapname(mapid):
        "returns mapname from a mapid"
        #maps stored in id: [name, notes]
        maps={1: ["Summoner's Rift", 'Original Summer variant'], 2: ["Summoner's Rift", 'Original Autumn variant'], 3: ['The Proving Grounds', 'Tutorial Map'], 4: ['Twisted Treeline', 'Original Version'], 8: ['The Crystal Scar', 'Dominion map'], 10: ['Twisted Treeline', 'Last TT map'], 11: ["Summoner's Rift", 'Current Version'], 12: ['Howling Abyss', 'ARAM map'], 14: ["Butcher's Bridge", 'Alternate ARAM map'], 16: ['Cosmic Ruins', 'Dark Star: Singularity map'], 18: ['Valoran City Park', 'Star Guardian Invasion map'], 19: ['Substructure 43', 'PROJECT: Hunters map'], 20: ['Crash Site', 'Odyssey: Extraction map'], 21: ['Nexus Blitz', 'Nexus Blitz map'], 22: ['Convergence', 'Teamfight Tactics map'], 30: ['Rings of Wrath', 'Arena map']}
        return maps[mapid][0]


    def itemsname(itemid):
        if itemid==0:
            return "-"
        url=f"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/item.json"
        r=requests.get(url).json()
        return r['data'][str(itemid)]['name']




class champion:
    """Functions used to ahndle champions"""
    def name(championID):
        championID=str(championID)
        "returns champion anme of given champion id"
        url="http://ddragon.leagueoflegends.com/cdn/13.18.1/data/en_US/championFull.json"
        r=requests.get(url).json()["keys"]
        name=r[championID]
        return str(name)
    
    def splashart(name):
        "returns url of champion splash art"
        url="http://ddragon.leagueoflegends.com/cdn/img/champion/splash/"+name+"_0.jpg"
        return url


    def square(name):
        url="http://ddragon.leagueoflegends.com/cdn/"+version+"/img/champion/"+name+".png"
        return url


##tester codes ***DELETE THESE***
# print(champion.name(25))
# print(champion.splashart("Morgana"))
# print(gameconstants.mapname(11))
# print(champion.square("Morgana"))