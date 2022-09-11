from django.shortcuts import render

# Create your views here.


def docente(request):
    return render(request, 'docente/docente.html')