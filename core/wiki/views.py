from django.shortcuts import render
from requests import get
from assets.riot import datadragon as datadragon





"""
-pass title as a var that holds the title of the page
    note that the var is set as SummonerForge|{{ title }}
    
"""
# Create your views here.

def home(request):
    title="Archive"
    return render(request, 'home.html', {
        'title': title
    })


def champions(request):
    champ_data=datadragon.Champion.fecthall()
    # x=[d['name'], d['title'], d['tags'], d['id']]
    return render(request, 'archive-champions.html', {
        'title': "Champions",
        'data' : champ_data,
    })






def champdescription(request, id):
    url=f"https://ddragon.leagueoflegends.com/cdn/{datadragon.version}/data/en_US/champion/"+ id +".json"

    data=get(url).json()
    champ=data['data'][id]

    title=champ['name']
    skins=champ['skins']


    #setting stat values

    #level
    l=[]
    for i in range(18):
        l.append(i+1)

    #hp
    hp=[]
    for i in range(18):
        hp.append(str(champ['stats']['hp'] + champ['stats']['hpperlevel']*i))

    #hp regen
    hpr=[]
    for i in range(18):
        hpr.append(str(round(champ['stats']['hpregen'] + champ['stats']['hpregenperlevel']*i,2)))
    
    #mp
    mp=[]
    for i in range(18):
        mp.append(str(champ['stats']['mp'] + champ['stats']['mpperlevel']*i))
    
    #hp regen
    mpr=[]
    for i in range(18):
        mpr.append(str(round(champ['stats']['mpregen'] + champ['stats']['mpregenperlevel']*i,2)))

    #armor
    armor=[]
    for i in range(18):
        armor.append(str(round(champ['stats']['armor'] + champ['stats']['armorperlevel']*i,2)))

    #spellblock
    spellblock=[]
    for i in range(18):
        spellblock.append(str(round(champ['stats']['spellblock'] + champ['stats']['spellblockperlevel']*i,2)))

    #Atk Damage
    atkD=[]
    for i in range(18):
        atkD.append(str(champ['stats']['attackdamage'] + champ['stats']['attackdamageperlevel']*i))

    #Atk speed
    atkS=[]
    for i in range(18):
        atkS.append(str(round(champ['stats']['attackspeed'] + champ['stats']['attackspeedperlevel']*i,2)))
    
    

    #combining them
    stats=[]
    for i in range(18):
        stats.append([l[i], hp[i], hpr[i], mp[i], mpr[i], atkD[i], atkS[i], armor[i], spellblock[i] ])


    return render(request, 'champion-description.html', {
        'title' : title,
        'champ' : champ,
        'skins' : skins,
        'stats' : stats,
    })







def items(request):
    title="items"
    return render(request, 'archive-items.html', {
        'title': title
    })