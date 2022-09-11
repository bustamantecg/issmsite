from django.shortcuts import render

# Create your views here.
from secretaria.models import Mesa, MesaDetalle


def alumnos(request):
    return render(request, "alumno/alumno.html")


def mesas_listado(request):
    mesas = Mesa.objects.filter(habilitada=True)
    return render(request, 'alumno/mesas_listado.html', {'mesas': mesas})


def mesas_detalles(request, id):
    mesaconsultada = Mesa.objects.get(pk=id)
    mesasdetalles = MesaDetalle.objects.filter(mesas=mesaconsultada)
    return render(request, 'alumno/mesas_detalle.html', {'mesaconsultada': mesaconsultada, 'mesasdetalles': mesasdetalles})


def alumno_perfil(request):
    return render(request, 'alumno/alumno_perfil.html')