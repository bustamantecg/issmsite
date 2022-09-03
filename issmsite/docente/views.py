from django.shortcuts import render

# Create your views here.


def docentes(request):
    return render(request, 'docente/docente.html')