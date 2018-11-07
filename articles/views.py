from django.shortcuts import render, redirect
from .models import Adoptante

# Create your views here.
def article_list(request):
    adoptantes = Adoptante.objects.all()
    return render(request, 'articles/article_list.html', {'adoptantes': adoptantes})


def adoptante_view(request):
    if request.metod == 'POST':
        form = AdoptanteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('adoptante:inicio')
    else:
        form = AdoptanteForm()

    return render(request, '/Formulario', {'form':form})
