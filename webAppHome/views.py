from django.shortcuts import render,HttpResponse #se importa esto


# Create your views here.
def home(request):
    return render(request, "home/index.html")
