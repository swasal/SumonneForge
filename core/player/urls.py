from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profilelanding, name="profilelanding"),
    path('searchsummoner/', views.searchsummoner, name="searchsummoner"),
    path('summonerprofile/<str:server>/<str:name>/<str:tag>', views.summonerprofile, name="summonerprofile"),
    # path('profile/<str:name>/<str:tag>', views.champions, name="profilesearch"),
    # path('/<str:p1>/<str:p2>/<str:p3>/<str:p4>', views.champdescription, name="multisearch"),

    
]
