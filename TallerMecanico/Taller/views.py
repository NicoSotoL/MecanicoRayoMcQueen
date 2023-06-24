from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login  # Renombrar la función login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db import IntegrityError
from .models import Publicacion
from .forms import PublicacionForm
from django.shortcuts import get_object_or_404


def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'lista_publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'detalle_publicacion.html', {'publicacion': publicacion})

def nueva_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = PublicacionForm()
    return render(request, 'nueva_publicacion.html', {'form': form})

def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            publicacion = form.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'editar_publicacion.html', {'form': form})

def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('lista_publicaciones')
    return render(request, 'eliminar_publicacion.html', {'publicacion': publicacion})

def index(request):
    context = {}
    return render(request, 'index.html', context)


def nosotros(request):
    context = {}
    return render(request, 'nosotros.html', context)


def agendar(request):
    context = {}
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
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                auth_login(request, user)  # Utilizar el nombre renombrado
                return redirect('index')    
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })

        return render(request, 'registro.html', {
            'form': UserCreationForm,
            "error": 'Contraseñas no coinciden'
        })
def modificar(request):
    context = {}
    return render(request, 'ModificarT.html', context)


def trabajos(request):
    context = {}
    return render(request, 'TrabajosR.html', context)


def eliminaragendamiento(request):
    context = {}
    return render(request, 'EliminarA.html', context)


@login_required
def indexA(request):
    context = {}
    return render(request, 'indexA.html', context)


@login_required
def indexM(request):
    context = {}
    return render(request, 'indexM.html', context)
