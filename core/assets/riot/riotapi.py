#imports
from os import getenv
from dotenv import load_dotenv
import requests





#getting the api from local machine 
load_dotenv()
api=getenv("riotAPI")



regions={
    'br1' : 'Brazil',
    'eun1' : 'Europe Nordic & East',
    'euw1' : 'Europe West',
    'jp1' : 'Japan',
    'kr' : 'Republic of Korea',
    'la1' : 'Latin America North',
    'la2' : 'Latin America South',
    'na1' : 'North America',
    'oc1' : 'Oceania',
    'tr1' : 'Turkey',
    'ru' : 'Russia',
    'ph2' : 'The Philippines',
    'sg2' : 'Singapore, Malaysia, & Indonesia',
    'th2' : 'Thailand',
    'tw2' : 'Taiwan, Hong Kong, and Macao',
    'vn2' : 'Vietnam',
}

class searchsummoner:
    """Search a sumonner by different keys.
    
    ***for testing the putp[ut***
    example code:

        for k,v in searchsummoner.bu_sumonnerID(summonerID, server).items():
        print(k,v)
    
    
    """

    def by_name(server, name, tag):
        "returns the basic stat of the summoner"
        #finds puuid
        payload={"api_key":api}
        url= f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}"
        r=requests.get(url, params=payload)
        puuid=r.json()['puuid']

        #using puuid to find summoner stats
        payload={"api_key":api}
        url= f"https://{server}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
        r=requests.get(url, params=payload)
        return r.json()


    

    def by_puuid(puuid,server):
        url="https://"+server+".api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+api
        r=requests.get(url).json()
        return r


    def by_accountID(account_ID, server):

        payload={"api_key":api}
        url= "https://" + server + ".api.riotgames.com/lol/summoner/v4/summoners/by-account/" + account_ID    
        r=requests.get(url, params=payload)
        return r.json()




class summonerStats:
    "used to access the player's profile stats history"

    




    def highestmastery(id, server):
        """highestmastery(id, server)
        returns stats for highest mastery champion"""
        url="https://"+str(server)+".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+str(id)+"?api_key="+str(api)
        r=requests.get(url)
        r=r.json()
        return r[0]
    

    def rank(summonerID: str, server):
        "returns ranked in solo and flex"
        url="https://"+server+".api.riotgames.com/lol/league/v4/entries/by-summoner/"+summonerID+"?api_key="+api
        r=requests.get(url).json()
        ranked={'flex':{}, 'solo':{}}
        if len(r)==0:
            ranked['flex']['rank']="Unranked"
            ranked['flex']['lp']="0"
            ranked['solo']['rank']="Unranked"
            ranked['solo']['lp']="0"

        elif len(r)==1:
            #only one rnaked queue hence set the other rank to none
            #finsing out which one is available RANKED_SOLO_5x5 or RANKED_FLEX_SR
            if r[0]['queueType']=="RANKED_SOLO_5x5": #set flex to none
                ranked['flex']['rank']="Unranked"
                ranked['flex']['lp']="0"
                ranked['solo']['rank']=r[0]['tier']+" "+ r[0]['rank']
                ranked['solo']['lp']=str(r[0]['leaguePoints'])

            if r[0]['queueType']=="RANKED_FLEX_SR": #set solo to none
                ranked['flex']['rank']=r[0]['tier']+" "+ r[0]['rank']
                ranked['flex']['lp']=str(r[0]['leaguePoints'])
                ranked['solo']['rank']="Unranked"
                ranked['solo']['lp']="0"

        else: #set ranked stats len==2
            if r[0]['queueType']=="RANKED_SOLO_5x5": #set flex to none
                ranked['flex']['rank']=r[1]['tier']+" "+ r[1]['rank']
                ranked['flex']['lp']=str(r[1]['leaguePoints'])
                ranked['solo']['rank']=r[0]['tier']+" "+ r[0]['rank']
                ranked['solo']['lp']=str(r[0]['leaguePoints'])


            else:
                ranked['flex']['rank']=r[0]['tier']+" "+ r[0]['rank']
                ranked['flex']['lp']=str(r[0]['leaguePoints'])
                ranked['solo']['rank']=r[1]['tier']+" "+ r[1]['rank']
                ranked['solo']['lp']=str(r[1]['leaguePoints'])

        return ranked


    def matchlist(server, puuid, count=10):
        region=summonerStats.region
        url="https://"+region[server.lower()]+".api.riotgames.com/lol/match/v5/matches/by-puuid/"+ puuid +"/ids?start=0&count="+str(count)+"&api_key="+api
        r=requests.get(url).json()
        return r
        
    
    def matchdetails(matchid):
        # might require to reroute regions for matchv4
        # if server in ['na1', 'br1', 'la1', 'la2']:
        #     server="americas"
        # elif server in ['jp1', 'kr', 'sg2']:
        #     server="asia"
        # elif server in ['eun1', 'euw1']:
        #     server="europe"
        # elif server in []:
        #     server="sea"
        # else:
        #     server="esports"


        region=summonerStats.region
        server=matchid.split("_")[0].lower()
        url="https://"+region[server]+".api.riotgames.com/lol/match/v5/matches/"+matchid+"?api_key="+api
        r=requests.get(url).json()
        return r
    
        



class Spectate:
    "INCOMPLETE: get live stats on summoner"
 



# testing codes here
# z=summonerStats.matchlist("eun1", "-uzcGyaoBjG7k3fGrHB8Bttg3lTsXaAa7N0U0H89D5wbWqxQjdkW_G_5LiVCY5N8mf_vQjGdwfF20g")

# z=summonerStats.matchdetails("EUN1_3455754572")
# r['info']['participants']
# print(z['info']['participants'][3]['item6'])
# print(datadragon)
# out=""
# for i in range(0,6):
#     out+=datadragon.gameconstants.itemsname(z['info']['participants'][3][f'item{i}'])+"\n"

# print(out)
# print(type(out))

# # # a=datetime.datetime.fromtimestamp(1694755285911)
# # # z['gameCreation']=a
# # # print(a)