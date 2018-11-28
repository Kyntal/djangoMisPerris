from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from articles.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required



def inicio(request):
    #return HttpResponse('Inicio')
    return render(request, 'inicio.html')

def login(request):

    return render(request, 'login.html')
def logout(request):
    return redirect('/')


def QuienSo(request):
    #return HttpResponse('about')
    return render(request, 'QuienSo.html')

def Formulario(request):
    return render(request, 'Formulario.html')

def Servicio(request):
    return render(request, 'Servicio.html')

def Contacto(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'Contacto.html',
                  {'user_form': user_form})

def Principal(request):
    return render(request, 'social.html')

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})
