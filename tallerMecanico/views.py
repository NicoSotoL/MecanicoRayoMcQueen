from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'tallerMecanico/index.html', context)

def nosotros(request):
    context={}
    return render(request, 'tallerMecanico/nosotros.html', context)

def agendar(request):
    context={}
    return render(request, 'tallerMecanico/agendar.html', context)

def login(request):
    context={}
    return render(request, 'tallerMecanico/login.html', context)

def registro(request):
    context={}
    return render(request, 'tallerMecanico/registro.html', context)

def modificar(request):
    context={}
    return render(request, 'tallerMecanico/ModificarT.html', context)

def trabajos(request):
    context={}
    return render(request, 'tallerMecanico/TrabajosR.html', context)

def eliminaragendamiento(request):
    context={}
    return render(request, 'tallerMecanico/EliminarA.html', context)
