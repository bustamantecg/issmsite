import smtplib
from django.shortcuts import render, redirect

# Create your views here.
from contacto.forms import FormularioContacto
from django.core.mail import EmailMessage
from django.conf import settings

#def contacto(request):
#    return render(request, 'contacto/contacto.html')

# https://techexpert.tips/es/python-es/python-enviar-correo-electronico-usando-gmail/


def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data=request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            #msg = EmailMessage()
            email = EmailMessage("Mensaje desde Contacto ISSM Site", 
                                 "el Usuario: {} con Email: {} \n te escribio: {}".format(nombre, email, contenido),
                                 "", ["bustamantecg@gmail.com"], reply_to=[email])
            s = smtplib.SMTP('smtp.gmail.com')
            s.send_message(email)
            s.quit()
            
            return redirect('/contacto/?valido')
            """

            
            email.send()
            return redirect('/contacto/?valido')
            #try:
                
            #except:
            
            """
        else:
            return redirect('/contacto/?novalido')           
    return render(request, 'contacto/contacto.html', {'form_contacto': formulario_contacto})