from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('producto',views.producto,name='producto'),
    path('videojuego',views.videojuego,name='videojuego'),
    path('rece',views.rece,name='rece'),
    path('consola',views.consola,name='consola'),
    path('maquina',views.maquina,name='maquina'),
]