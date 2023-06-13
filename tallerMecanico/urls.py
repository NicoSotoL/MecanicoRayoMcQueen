from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index.html/', views.index, name='index_html'),
    path('Nosotros.html/', views.nosotros, name='nosotros_html'),
]
