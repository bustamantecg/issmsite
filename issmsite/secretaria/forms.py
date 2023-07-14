from django import forms
from django.forms import TextInput, EmailInput

from secretaria.models import Alumno, Persona, Carrera


class PersonaForm(forms.ModelForm):
    class Meta:
        
        model = Persona
        fields = '__all__'
        widgets = {
            'dni': TextInput(attrs={'class': 'form-control'}),
            'apellido': TextInput(attrs={'class': 'form-control'}),
            'nombre': TextInput(attrs={'class': 'form-control'}),
            #'fechanac': TextInput(attrs={'class': 'form-control', 'localize':True}),
 
            'fechanac' : forms.DateInput(attrs={'type': 'date'}),   
            'domicilio': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'type': 'email'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Foto'
                }
            )
        }


class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'})
        }

class AlumnoInscripCarreraForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['carrera', 'persona', 'ingreso', 'legajo']
        #fields = '__all__'

        widgets = {
            'carrera': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione Carrera'
                }
            ),
            'persona': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione Persona'
                }
            ),
            'ingreso' : forms.DateInput(attrs={'type': 'date'})   
            
        }