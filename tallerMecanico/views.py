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
