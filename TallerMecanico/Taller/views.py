from django.shortcuts import render
from django.http import HttpResponse
from .Resennas import generar_resennas_azar
from .forms import ContactoForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            context = {'mensaje': "owo"}
        else:
            context = {'error': "unu"}
    else:
        formulario = ContactoForm()
        context = {'form': formulario}

    return render(request, 'Contacto.html', context)


def generar_resennas(request):
    cantidad = 10
    generar_resennas_azar(cantidad)
    return HttpResponse("Reseñas generadas con éxito.")


def index(request):
    context = {}
    return render(request, 'index.html', context)


def nosotros(request):
    context = {}
    return render(request, 'nosotros.html', context)


def agendar(request):
    context = {}
    return render(request, 'agendar.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def registro(request):
    context = {}
    return render(request, 'registro.html', context)


def modificar(request):
    context = {}
    return render(request, 'ModificarT.html', context)


def trabajos(request):
    context = {}
    return render(request, 'TrabajosR.html', context)


def eliminaragendamiento(request):
    context = {}
    return render(request, 'EliminarA.html', context)

