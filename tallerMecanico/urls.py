from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('agendar/', views.agendar, name='agendar'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
]
