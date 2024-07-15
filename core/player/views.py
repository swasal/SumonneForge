from django.shortcuts import render, redirect, reverse
from requests import get
from assets.riot.riotapi import regions, searchsummoner


# Create your views here.

def profilelanding(request): #the search page with the summoner

    return render(request, 'playersearch.html', {

    })




def searchsummoner(request): #link from the search form
    if request.method=="POST":
        name=request.POST.get("name")
        tag=request.POST.get("tag")
        server=request.POST.get("server")
    
    
    return redirect(f'summonerprofile/{server}/{name}/{tag}')




def summonerprofile(request, server, name, tag): #lands on the summoner profile page
    
    summoner=searchsummoner.by_name(server, name, tag)
    puuid=summoner['puuid']
    profileicon=summoner['profileIconId']
    level=summoner['summonerLevel']


    
    
    return
