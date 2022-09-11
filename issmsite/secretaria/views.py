from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
from secretaria.models import Carrera, Materia, Alumno, Persona, Docente

#--------------Views para Secretaria -----------------------------------------------------#


@login_required
def secretaria(reeques):
    return render(reeques, 'secretaria/secretaria.html')


#--------------Views para Carrreras---------------------------------------------------------#

def carreras_listado(request):
    carreras = Carrera.objects.order_by('nombre')
    return render(request, 'secretaria/carreras_listado.html', {'carreras': carreras})


def carrera_listado(request):
    busqueda = request.POST.get('buscar')
    carreras = Carrera.objects.all().order_by('nombre')
    cantidad = len(carreras)
    if busqueda:
        carreras = Carrera.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(legal__icontains=busqueda) |
            Q(cuatrimestre__icontains=busqueda) |
            Q(tipo__icontains=busqueda) |
            Q(duracion__icontains=busqueda)
        ).distinct().order_by('nombre')
    return render(request, 'secretaria/carrera_listado.html', {'carreras': carreras, 'cantidad': cantidad})


def carreras_detalle(request, id):
    carrera = Carrera.objects.get(pk=id)
    materias = Materia.objects.filter(carrera_id=id).order_by('cuatrimestre', 'nombre')
    canti_materias = Materia.objects.filter(carrera_id=id).count()
    return render(request, 'secretaria/carreras_detalle.html', {'carrera': carrera, 'materias': materias, 'canti_materias': canti_materias})


#--------------Views para Alumnos ---------------------------------------------------------#

def alumno_listado(request):
    busqueda = request.POST.get('buscar')
    personas = Alumno.objects.all().order_by('persona__apellido', 'persona__nombre')
    cantidad = len(personas)
    if busqueda:
        personas = Docente.objects.filter(
            Q(persona__dni__icontains=busqueda) |
            Q(persona__apellido__icontains=busqueda) |
            Q(persona__nombre__icontains=busqueda) |
            Q(persona__domicilio__icontains=busqueda) |
            Q(titulo__icontains=busqueda) |
            Q(legajo__icontains=busqueda) |
            Q(persona__email__icontains=busqueda)
        ).distinct().order_by('persona__apellido')
    return render(request, 'secretaria/alumno_listado.html', {'personas': personas, 'cantidad': cantidad})


def alumno_consulta(request):
    return render(request, 'secretaria/alumno_consulta.html')


def buscar_alumno_dni(request):
    if request.GET['dni']:
        dnibuscar = request.GET['dni']
        persona = Persona.objects.get(dni=dnibuscar)
        alumno = Alumno.objects.filter(persona=persona)

        carreras = Carrera.objects.filter(nombre__contains=alumno)
                #query = Alumno.objects.filter(persona__dni=dni).filter(carrera_id=Carrera.id)
        #return render(request, 'secretaria/alumno_resul_dni.html', {'persona': persona, 'query_dni': dni, 'alumno': alumno})
        return render(request, 'secretaria/alumno_resul_dni.html', {'persona': persona, 'query_dni': dni, 'alumno': alumno, 'carreras':carreras})
    else:
        mensaje = 'No ingreso D.N.I. del alumno/a a consultar'

    return HttpResponse(mensaje)


#--------------Views para Docentes---------------------------------------------------------#
def docentes_listado(request):
    busqueda = request.POST.get('buscar')
    personas = Docente.objects.all().order_by('persona__apellido')
    cantidad = len(personas)
    encontrados = cantidad
    if busqueda:
        personas = Docente.objects.filter(
            Q(persona__dni__icontains=busqueda) |
            Q(persona__apellido__icontains=busqueda) |
            Q(persona__nombre__icontains=busqueda) |
            Q(persona__domicilio__icontains=busqueda) |
            Q(titulo__icontains=busqueda) |
            Q(legajo__icontains=busqueda) |
            Q(persona__email__icontains=busqueda)
        ).distinct().order_by('persona__apellido')
        encontrados = len(personas)
    return render(request, 'secretaria/docentes_listado.html', {'personas': personas, 'cantidad': cantidad, 'encontrados':encontrados})