from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
# Create your views here.
from django.views.generic import TemplateView

from secretaria.models import Carrera


def index(request):
    return render(request, 'homeapp/index.html')

def about(request):
    return render(request, 'homeapp/about.html')

@login_required
def home(request):
    if request.user.is_authenticated:
        # grupete = request.user.groups.all()
        # resultado = request.user.groups.filter(name='Estudiantes').exists()
        # return render(request, 'alumno/alumno.html', {'grupete': grupete, 'resultado': resultado})
        return render(request, 'homeapp/home.html')
    else:
        return render(request, 'homeapp/home.html')


class Error404View(TemplateView):
    templates_name = 'homeapp/error_404.html'