from django.shortcuts import render, redirect, reverse
from requests import get
from assets.riot.riotapi import searchsummoner, summonerStats


# Create your views here.

def profilelanding(request): #the search page with the summoner

    return render(request, 'playersearch.html', {

    })




def summonersearch(request): #link from the search form
    if request.method=="POST":
        name=request.POST.get("name")
        tag=request.POST.get("tag")
        server=request.POST.get("server")
    
    
    # return redirect(f'summonerprofile/{server}/{name}/{tag}')
    return redirect('summonerprofile', server=server, name=name, tag=tag)




def summonerprofile(request, server, name, tag): #lands on the summoner profile page
    
    summoner=searchsummoner.by_name(server, name, tag)

    rank=summonerStats.rank(summoner["id"], server)

    puuid=summoner['puuid']
    profileicon=summoner['profileIconId']
    level=summoner['summonerLevel']
    matches=summonerStats.matchlist(server,puuid,20)

    return render(request, 'playerprofile.html', {
        'puuid': puuid,
        'profileicon' : profileicon,
        'level' : level,
        'name' : name,
        'tag' : tag,
        'rank':rank,
        'matches':matches,
    })