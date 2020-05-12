from django.shortcuts import render
from .models import *

#pagina inicial do site, exibe das 10 ultimas postagens
def home(request):
    template = 'home.html'
    sessoes = Sessao.objects.all()
    postagens = Postagem.objects.all()
    context = {
        "sessoes" : sessoes,
        "postagens" : postagens
    }
    return render(request, template, context)

#pagina que irá renderizar as sessoes cadastradas no blog
def sessao(request, slug):
    template = 'sessao.html'
    sessoes = Sessao.objects.all()
    sessaoAtual = Sessao.objects.filter(slug=slug).first()
    postagens = Postagem.objects.filter(sessao=sessaoAtual, postar=True)
    context = {
        "sessao" : sessaoAtual,
        "sessoes" : sessoes,
        "postagens" : postagens
    }
    return render(request, template, context)

#pagina que irá renderizar as postagens
def postagem(request, slugSessao, slugPostagem):
    template = 'postagem.html'
    return render(request, template)
