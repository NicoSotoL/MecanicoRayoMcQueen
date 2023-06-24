from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('indexA/', views.indexA, name='indexA'),
    path('indexM/', views.indexM, name='indexM'),
    path('agendar/', views.agendar, name='agendar'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('modificar/', views.modificar, name='modificar'),
    path('trabajos/', views.trabajos, name='trabajos'),
    path('eliminaragendamiento/', views.eliminaragendamiento, name='eliminaragendamiento'),
    path('pruebas/', views.pruebas, name='pruebas'),
]