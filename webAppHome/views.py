from django.shortcuts import render,HttpResponse #se importa esto
from personasApp.models import *

# Create your views here.
def home(request):
    #personas =Personas.objects.all() Esto es para que muestre todas las personas en la BD
    personas =Personas.objects.order_by('id')# por defaul se ordena de forma acendente si queremos lo contrario agregamos('-id')- o
    # se puede agregar mas ordenamientos personas =Personas.objects.order_by('id','nombre')
    mensaje={'msg':'hola a todos view','msg2':'este es el segundo'}
    return render(request, "home/index.html",{'personas':personas})
