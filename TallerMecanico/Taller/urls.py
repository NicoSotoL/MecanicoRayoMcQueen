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
    path('publicaciones/', views.lista_publicaciones, name='lista_publicaciones'),
    path('publicaciones/nueva/', views.nueva_publicacion, name='nueva_publicacion'),
    path('publicaciones/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('publicaciones/<int:pk>/editar/', views.editar_publicacion, name='editar_publicacion'),
    path('publicaciones/<int:pk>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),

]