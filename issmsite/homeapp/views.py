from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from secretaria.models import Carrera


@login_required
def home(request):
    return render(request, 'homeapp/home.html')
