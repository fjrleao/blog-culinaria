from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import *

#pagina inicial do site, exibe das 10 ultimas postagens
def home(request):
    template = 'home.html'
    sessoes = Sessao.objects.all()
    postagens = Postagem.objects.filter(postar=True)
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

@csrf_protect
def comentar(request, slugSessao, slugPostagem):
    if request.POST:
        nome = request.POST.get('nome')
        comentario = request.POST.get('comentario')
        nota = request.POST.get('nota')
        p = Postagem.objects.get(slug=slugPostagem)
        c = Comentario(nome=nome, texto=comentario, avaliacao=nota, postagem=p)
        c.save()

    return redirect(postagem, slugSessao, slugPostagem)