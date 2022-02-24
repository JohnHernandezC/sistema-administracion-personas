#con esto se personaliza los forms
from django.forms import EmailInput, ModelForm
from personasApp.models import Personas


class PersonaForm(ModelForm):
    class Meta:
        model=Personas
        fields='__all__'
        widget={
            'email':EmailInput(attrs={'type': 'email'})
        }