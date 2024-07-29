from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profilelanding, name="profilelanding"),
    path('searchsummoner/', views.summonersearch, name="summonersearch"),
    path('summonerprofile/<str:server>/<str:name>/<str:tag>', views.summonerprofile, name="summonerprofile"),

    
]
