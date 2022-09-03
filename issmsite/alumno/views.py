from django.shortcuts import render

# Create your views here.
from secretaria.models import Mesa


def alumnos(request):
    return render(request, "alumno/alumno.html")


def mesas_listado(request):
    mesas = Mesa.objects.filter(habilitada=True)
    return render(request, 'alumno/mesas_listado.html', {'mesas': mesas})


def alumno_perfil(request):
    return render(request, 'alumno/alumno_perfil.html')