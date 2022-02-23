from django.shortcuts import render,HttpResponse #se importa esto
from personasApp.models import *

# Create your views here.
def home(request):
    personas =Personas.objects.all()
    mensaje={'msg':'hola a todos view','msg2':'este es el segundo'}
    return render(request, "home/index.html",{'personas':personas})
