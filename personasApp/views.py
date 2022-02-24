from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from personasApp.forms import PersonaForm

from personasApp.models import Personas

# Create your views here.
def detallePersona(request, id):
    #persona=Personas.objects.get(pk=id)
    persona=get_object_or_404(Personas,pk=id)
    #solicita los datos pero si el id no esta presente devuelve el 404
    return render(request, 'personas/detalle.html',{'persona':persona}) 

#se remplaza esto por lo de la clase forms y se importa
#PersonaForm=modelform_factory(Personas, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona=PersonaForm(request.POST)#obtener la informacion que esta cntenida en el metodo POST 
        #de ls vista nuevo
        if formaPersona.is_valid():#validar si el formulario es valido
            formaPersona.save()
            return redirect('index')
        
    else:
        formaPersona=PersonaForm()
    return render(request, 'personas/nuevo.html',{'formaPersona':formaPersona})

def editarPersona(request,id):
    persona=get_object_or_404(Personas,pk=id)
    if request.method == 'POST':
        formaPersona=PersonaForm(request.POST, instance=persona)#obtener la informacion que esta cntenida en el metodo POST 
        #de ls vista nuevo
        if formaPersona.is_valid():#validar si el formulario es valido
            formaPersona.save()
            return redirect('index')
        
    else:
        
        formaPersona=PersonaForm(instance=persona)
        
    return render(request, 'personas/editar.html',{'formaPersona':formaPersona})

def eliminarPersona(request,id):
    persona=get_object_or_404(Personas,pk=id)
    if persona:
        persona.delete()
    return redirect('index')
        
    
    