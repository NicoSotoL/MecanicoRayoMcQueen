from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from .Resennas import generar_resennas_azar
from .models import Mecanico
from django.views.decorators.csrf import csrf_protect

def generar_resennas(request):
    cantidad = 10 
    generar_resennas_azar(cantidad)
    return HttpResponse("Reseñas generadas con éxito.")

def index(request):
    context={}
    return render(request, 'index.html', context)

def login1(request):
    context={}
    return render(request, 'login1.html', context)

def nosotros(request):
    context={}
    return render(request, 'nosotros.html', context)

def agendar(request):
    context={}
    return render(request, 'agendar.html', context)

@csrf_protect
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('indexA')
            elif user.is_mecanico:
                return redirect('indexM')
            else:
                return redirect('indexU')
        else:
            error_message = "Credenciales inválidas. Por favor, inténtalo de nuevo."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def registro(request):
    context={}
    return render(request, 'registro.html', context)

def modificar(request):
    context={}
    return render(request, 'ModificarT.html', context)

def trabajos(request):
    context={}
    return render(request, 'TrabajosR.html', context)

def eliminaragendamiento(request):
    context={}
    return render(request, 'EliminarA.html', context)

def pruebas(request):
    mecanicosList = Mecanico.objects.all()
    return render(request, 'Pruebas.html', {"mecanicos":mecanicosList})

def indexA(request):
    context={}
    return render(request, 'indexA.html', context)

def indexM(request):
    context={}
    return render(request, 'indexM.html', context)