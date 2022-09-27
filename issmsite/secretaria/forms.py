from django import forms
from django.forms import EmailInput

from secretaria.models import Alumno, Persona, Docente


class PersaonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'carrera': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione Carrera'
                }
            ),
            'email': EmailInput(attrs={'type':'email'})
        }


class AlumnoInscripCarreraForm(forms.ModelForm):
    class Meta:
        model = Alumno
        #fields = ['carrera', 'persona', 'ingreso', 'foto', 'legajo']
        fields = '__all__'

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
            'ingreso': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Fecha de Ingreso'
                },
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Foto'
                }
            )
        }


class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        widgets = {
            'carreras': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione las Carreras'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Foto',
                    'upload_to' : 'docente'
                }
            )
        }