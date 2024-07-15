from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('archive-champions/', views.champions, name="champions"),
    path('archive-champion/<str:id>', views.champdescription, name="champdescription"),

    path('archive-items/', views.items, name="items"),
    
]
