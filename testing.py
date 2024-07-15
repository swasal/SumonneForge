from core.assets.riot.riotapi import searchsummoner

x=searchsummoner.by_name('sg2', 'swasal','sg2')
for k,v in x.items():
    print(f"{k} : {v}")