from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from docente.forms import DocenteForm
from docente.forms import DocenteForm2
from secretaria.models import Docente


def docente(request):
    return render(request, 'docente/docente.html')

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
    return render(request, 'docente/docente_listado.html', data)

def docente_crear(request):
    if request.method == 'POST':
        formaDocenteCrear = DocenteForm2(request.POST, request.FILES)
        if formaDocenteCrear.is_valid():

            formaDocenteCrear.save()
            return redirect('docente_listado')
    else:
        formaDocenteCrear = DocenteForm2()
    return render(request, 'docente/docente_crear.html',{'formaDocenteCrear': formaDocenteCrear})


def docente_detalle(request, id):
    docente = get_object_or_404(Docente, pk=id)
    return render(request, 'docente/docente_detalle.html', {'docente':docente, 'id':id})