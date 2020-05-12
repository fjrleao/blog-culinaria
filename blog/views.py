from django.shortcuts import render
from .models import Sessao

def home(request):
    template = 'home.html'
    sessoes = Sessao.objects.all()
    context = {
        "sessoes" : sessoes
    }
    return render(request, template, context)