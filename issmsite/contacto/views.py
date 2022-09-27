from django.shortcuts import render, redirect

# Create your views here.
from contacto.forms import FormularioContacto


def contacto(request):
    return render(request, 'contacto/contacto.html')


def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data=request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            return redirect('/contacto/?valido')

    return render(request, 'contacto/contacto.html', {'form_contacto': formulario_contacto})