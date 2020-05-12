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
    sessaoAtual = Sessao.objects.get(slug=slug)
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
    sessoes = Sessao.objects.all()
    postagem = Postagem.objects.get(slug=slugPostagem)
    context = {
        "sessoes" : sessoes,
        "postagem" : postagem
    }
    return render(request, template, context)
