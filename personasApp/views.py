from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, render

from personasApp.models import Personas

# Create your views here.
def detallePersona(request, id):
    #persona=Personas.objects.get(pk=id)
    persona=get_object_or_404(Personas,pk=id)
    #solicita los datos pero si el id no esta presente devuelve el 404
    return render(request, 'personas/detalle.html',{'persona':persona}) 
PersonaForm=modelform_factory(Personas, exclude=[])
def nuevaPersona(request):
    formaPersona=PersonaForm()
    return render(request, 'personas/nuevo.html',{'formaPersona':formaPersona})
    