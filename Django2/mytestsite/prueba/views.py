from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Bienvenidos a mi sitio de prueba</h1>")
    Urls.py