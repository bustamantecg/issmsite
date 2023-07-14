from django import forms
from django.forms import EmailInput, ValidationError


from secretaria.models import Docente


class DocenteForm2(forms.ModelForm):
    """
    persona = 
    def clean_persona(self):
        persona = self.cleaned_data["persona"]
        existe = Docente.objects.filter(persona=Docente.persona).exists()

        if existe:
            raise ValidationError("Ya Existe Docente")
        
        return 

    """
    class Meta:
        model = Docente
        fields = ('persona', 'legajo', 'titulo', 'horas_catedras', 'legajo')

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        widgets = {
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Foto',
                    'upload_to': 'docente/'
                }
            )
        }