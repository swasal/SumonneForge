"""Used to interact with riot's centralized database for league.
refer to => https://developer.riotgames.com/docs/lol#data-dragon

***NOTE***
This uses their online databse with the requests library.
"""

#imports
import requests
from typing import List, Dict, Optional



#checking for the latest datadragon version
url = "https://ddragon.leagueoflegends.com/api/versions.json"
r = requests.get(url)
version = r.json()[0]





class profile:
    """Initializing the python"""
    @staticmethod
    def icon(id: int) -> str:
        "returns url to profile icon of the given id"
        url = "http://ddragon.leagueoflegends.com/cdn/" + str(version) + "/img/profileicon/" + str(id) + ".png"
        return url





class gameconstants:
    "gameconstants used by riot api from datadragon"



    @staticmethod
    def mapname(mapid: int) -> str:
        "returns mapname from a mapid"
        #maps stored in id: [name, notes]
        maps = {1: ["Summoner's Rift", 'Original Summer variant'], 2: ["Summoner's Rift", 'Original Autumn variant'], 3: ['The Proving Grounds', 'Tutorial Map'], 4: ['Twisted Treeline', 'Original Version'], 8: ['The Crystal Scar', 'Dominion map'], 10: ['Twisted Treeline', 'Last TT map'], 11: ["Summoner's Rift", 'Current Version'], 12: ['Howling Abyss', 'ARAM map'], 14: ["Butcher's Bridge", 'Alternate ARAM map'], 16: ['Cosmic Ruins', 'Dark Star: Singularity map'], 18: ['Valoran City Park', 'Star Guardian Invasion map'], 19: ['Substructure 43', 'PROJECT: Hunters map'], 20: ['Crash Site', 'Odyssey: Extraction map'], 21: ['Nexus Blitz', 'Nexus Blitz map'], 22: ['Convergence', 'Teamfight Tactics map'], 30: ['Rings of Wrath', 'Arena map']}
        return maps[mapid][0]



    @staticmethod
    def itemsname(itemid: int) -> str:
        if itemid == 0:
            return "-"
        url = f"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/item.json"
        r = requests.get(url).json()
        return r['data'][str(itemid)]['name']





class Champion:
    """Class with champion related data handling"""

    def __init__(
                self,
                champid: Optional[str] = None,    
                name: Optional[str] = None,       
                title: Optional[str] = None,      
                skins: Optional[List[Dict]] = None,      # List of available skins for the champion
                lore: Optional[str] = None,       # Backstory or lore about the champion
                blurb: Optional[str] = None,      # A short description or summary of the champion
                allytips: Optional[List[str]] = None,   
                enemytips: Optional[List[str]] = None,  
                tags: Optional[List[str]] = None,       # Tags/categories for the champion (e.g., Fighter, Mage, etc.)
                partype: Optional[str] = None,    # Resource type used by the champion (e.g., Mana, Energy, etc.)
                info: Optional[Dict] = None,       # Difficulty rating 
                stats: Optional[Dict] = None,      # Detailed stats like health, armor, attack speed, etc.
                spells: Optional[List[Dict]] = None,     # List of the champion's active spells
                passive: Optional[Dict] = None,    # The champion's passive ability
                ):
        
        self.champid = champid
        self.name = name
        self.title = title
        self.skins = skins
        self.lore = lore
        self.blurb = blurb
        self.allytips = allytips
        self.enemytips = enemytips
        self.tags = tags
        self.partype = partype
        self.info = info
        self.stats = stats
        self.spells = spells
        self.passive = passive
        self.imageloading = Champion.generateImagelink('champion', f"{name}.png", 'loading')



    class Spells:
        def __init__(
                    self, 
                    spell_id: Optional[str] = None,
                    name: Optional[str] = None,
                    description: Optional[str] = None,
                    maxrank: Optional[int] = None,
                    cooldownBurn: Optional[str] = None,
                    costBurn: Optional[str] = None,
                    rangeBurn: Optional[str] = None,
                    ):
        
            self.spell_id = spell_id
            self.name = name
            self.description = description
            self.maxrank = maxrank
            self.cooldownBurn = cooldownBurn
            self.costBurn = costBurn
            self.rangeBurn = rangeBurn




    class Stats:
        def __init__(
                    self, 
                    hp: Optional[float] = None, 
                    hpperlevel: Optional[float] = None, 
                    mp: Optional[float] = None, 
                    mpperlevel: Optional[float] = None, 
                    movespeed: Optional[float] = None, 
                    armor: Optional[float] = None, 
                    armorperlevel: Optional[float] = None, 
                    spellblock: Optional[float] = None, 
                    spellblockperlevel: Optional[float] = None, 
                    attackrange: Optional[float] = None, 
                    hpregen: Optional[float] = None, 
                    hpregenperlevel: Optional[float] = None, 
                    mpregen: Optional[float] = None, 
                    mpregenperlevel: Optional[float] = None, 
                    crit: Optional[float] = None, 
                    critperlevel: Optional[float] = None, 
                    attackdamage: Optional[float] = None, 
                    attackdamageperlevel: Optional[float] = None, 
                    attackspeed: Optional[float] = None,
                    attackspeedperlevel: Optional[float] = None
                    ):
            
            self.hp = hp
            self.hpperlevel = hpperlevel
            self.mp = mp
            self.mpperlevel = mpperlevel
            self.movespeed = movespeed
            self.armor = armor
            self.armorperlevel = armorperlevel
            self.spellblock = spellblock
            self.spellblockperlevel = spellblockperlevel
            self.attackrange = attackrange
            self.hpregen = hpregen
            self.hpregenperlevel = hpregenperlevel
            self.mpregen = mpregen
            self.mpregenperlevel = mpregenperlevel
            self.crit = crit
            self.critperlevel = critperlevel
            self.attackdamage = attackdamage
            self.attackdamageperlevel = attackdamageperlevel
            self.attackspeed = attackspeed
            self.attackspeedperlevel = attackspeedperlevel



    class Passive:
        def __init__(
                    self,
                    name: Optional[str] = None,
                    description: Optional[str] = None,
                    image: Optional[Dict] = None
                    ):
            
            self.name = name
            self.description = description
            self.image = image



    @staticmethod
    def generateImagelink(group: str, name: str, subgroup: Optional[str] = None) -> str:
        "Returns the url to the image"
        if subgroup:
            url = f"https://ddragon.leagueoflegends.com/cdn/{version}/img/{group}/{subgroup}/{name}"
        else:
            url = f"https://ddragon.leagueoflegends.com/cdn/{version}/img/{group}/{name}"
        
        return url



    @staticmethod
    def fecthall() -> List['Champion']:
        "returns "
        url = f"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
        rawdata = requests.get(url).json()['data']
        championNameList = rawdata.keys()
        champdatalist = []

        for champ in championNameList:
            champdata = rawdata[champ]
            data = Champion(champid=champdata['id'], name=champdata['name'], title=champdata['title'], tags=champdata['tags'])
            champdatalist.append(data)

        return champdatalist



    @staticmethod
    def champion_detail(championid: str) -> 'Champion':
        url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{championid}.json"
        # http://ddragon.leagueoflegends.com/cdn/15.1.1/data/en_US/champion.json
        data = requests.get(url).json()['data'][championid]
        stats = data['stats']
        championdata = Champion(
                champid = data['id'],
                name = data['name'],
                title = data['title'],
                tags = data['tags'],
                partype = data['partype'],
                info = data['info'],
                lore = data['lore'],
                allytips = data['allytips'],
                enemytips = data['enemytips'],
                stats = stats,
                spells = data.get('spells'),
                passive = data.get('passive')
                )
        
        return championdata
