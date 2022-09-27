from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
# Create your views here.
from secretaria.forms import AlumnoInscripCarreraForm, DocenteForm
from secretaria.models import Carrera, Materia, Alumno, Persona, Docente, Empleado


#--------------Views para Secretaria -----------------------------------------------------#

@login_required
def secretaria(reeques):
    return render(reeques, 'secretaria/secretaria.html')


#--------------Views para Carrreras---------------------------------------------------------#
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


#--------------Views para Alumnos ---------------------------------------------------------

def alumno_listado(request):
    busqueda = request.GET.get('buscar')
    personas = Alumno.objects.all().order_by('persona__apellido', 'persona__nombre')
    cantidad = len(personas)
    paginate_by = 3
    if busqueda:
        personas = Alumno.objects.filter(
            Q(persona__dni__icontains=busqueda) |
            Q(persona__apellido__icontains=busqueda) |
            Q(persona__nombre__icontains=busqueda) |
            Q(persona__domicilio__icontains=busqueda) |
            Q(legajo__icontains=busqueda) |
            Q(persona__email__icontains=busqueda)
        ).distinct().order_by('persona__apellido')

        paginacion = Paginator(personas, 4)
        page = request.GET.get('page')
        personas = paginacion.get_page(page)

    return render(request, 'secretaria/alumno_listado.html', {'personas': personas, 'cantidad': cantidad})


def alumno_inscribir_carrera(request):
    if request.method == 'POST':
        formaAlumnoInscripCarrera = AlumnoInscripCarreraForm(request.POST)
        if formaAlumnoInscripCarrera.is_valid():
            formaAlumnoInscripCarrera.save()
            return redirect('secretaria.html')
    else:
        formaAlumnoInscripCarrera = AlumnoInscripCarreraForm()
    return render(request, 'secretaria/alumno_inscribir_carrera.html',{'formaAlumnoInscripCarrera': formaAlumnoInscripCarrera})


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
        return render(request, 'secretaria/alumno_resul_dni.html', {'persona': persona, 'query_dni': dnibuscar, 'alumno': alumno, 'carreras':carreras})
    else:
        mensaje = 'No ingreso D.N.I. del alumno/a a consultar'

    return HttpResponse(mensaje)


#--------------Views para Docentes---------------------------------------------------------#
def docente_listado(request):
    page = request.GET.get('page', 1)
    docentes = Docente.objects.all().order_by('persona__apellido')
    cantidad = len(docentes)

    try:
        paginator = Paginator(docentes, 2)
        docentes = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': docentes,
        'paginator': paginator,
        'cantidad': cantidad
    }
    return render(request, 'secretaria/docente_listado.html', data)


def docente_crear(request):
    if request.method == 'POST':
        formaDocenteCrear = DocenteForm(request.POST)
        if formaDocenteCrear.is_valid():
            formaDocenteCrear.save()
            return redirect('docente_listado')
    else:
        formaDocenteCrear = DocenteForm()
    return render(request, 'secretaria/docente_crear.html',{'formaDocenteCrear': formaDocenteCrear})


#--------------Views para Empleados de la Institutcion -----------------------------------------------#
def empleado_listado(request):
    busqueda = request.POST.get('buscar')
    empleados = Empleado.objects.all().order_by('persona__apellido')
    cantidad = len(empleados)
    encontrados = cantidad
    if busqueda:
        empleados = Empleado.objects.filter(
            Q(persona__dni__icontains=busqueda) |
            Q(persona__apellido__icontains=busqueda) |
            Q(persona__nombre__icontains=busqueda) |
            Q(cargo__icontains=busqueda) |
            Q(persona__email__icontains=busqueda)
        ).distinct().order_by('persona__apellido', 'persona__nombre')
        encontrados = len(empleados)
    return render(request, 'secretaria/empleado_listado.html', {'empleados': empleados, 'cantidad': cantidad, 'encontrados':encontrados})


#--------------Views para Personas---------------------------------------------------------#
def personas_listado(request):
    busqueda = request.POST.get('buscar')
    personas = Persona.objects.all().order_by('apellido', 'nombre')
    cantidad = len(personas)
    encontrados = cantidad
    if busqueda:
        personas = Persona.objects.filter(
            Q(dni__icontains=busqueda) |
            Q(apellido__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(dni__icontains=busqueda) |
            Q(email__icontains=busqueda)
        ).distinct().order_by('apellido', 'nombre')
        encontrados = len(personas)
    return render(request, 'secretaria/persona_listado.html', {'personas': personas, 'cantidad': cantidad, 'encontrados':encontrados})


