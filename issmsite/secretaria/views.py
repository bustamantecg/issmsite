from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from secretaria.models import Carrera, Materia


@login_required
def secretaria(reeques):
    return render(reeques, 'secretaria.html')


def carreras_listado(request):
    carreras = Carrera.objects.order_by('nombre')
    return render(request, 'carreras_listado.html', {'carreras': carreras})


def carreras_detalle(request, id):
    carrera = Carrera.objects.get(pk=id)
    materias = Materia.objects.filter(carrera_id=id).order_by('cuatrimestre', 'nombre')
    canti_materias = Materia.objects.filter(carrera_id=id).count()
    return render(request, 'carreras_detalle.html', {'carrera': carrera, 'materias': materias, 'canti_materias': canti_materias})


def alumnos_lisatdo(request):
  #  alumnos = Alumnos.objects.order_by('Apellido', 'nombre')
    pass