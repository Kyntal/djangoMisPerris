<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    #return HttpResponse('Inicio')
    return render(request, 'inicio.html')

def QuienSo(request):
    #return HttpResponse('about')
    return render(request, 'QuienSo.html')

def Formulario(request):
    return render(request, 'Formulario.html')

def Servicio(request):
    return render(request, 'Servicio.html')

def Contacto(request):
    return render(request, 'Contacto.html')
=======
from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    #return HttpResponse('Inicio')
    return render(request, 'inicio.html')

def QuienSo(request):
    #return HttpResponse('about')
    return render(request, 'QuienSo.html')

def Formulario(request):
    return render(request, 'Formulario.html')

def Servicio(request):
    return render(request, 'Servicio.html')

def Contacto(request):
    return render(request, 'Contacto.html')
>>>>>>> c6095b82dfc81f997d4028bbd5e94d7997ce1502
