from core.assets.riot.riotapi import searchsummoner, summonerStats

summoner=searchsummoner.by_name('sg2', 'swasal','sg2')
summoner['puuid']
print(summoner['puuid'])
# matches=summonerStats.matchlist('sg2',summoner['puuid'],20)
# for k,v in summoner.items():
#     print(f"{k} : {v}")

# rank=summonerStats.rank(summoner["id"], 'sg2')
# print(rank)