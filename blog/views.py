from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import *

#pagina inicial do site, exibe das 10 ultimas postagens
def home(request):
    template = 'home.html'
    sessoes = Sessao.objects.all()
    postagens = Postagem.objects.filter(postar=True).order_by('-data')[:10]
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
    postagens = Postagem.objects.filter(sessao=sessaoAtual, postar=True).order_by('-data')
    if postagens:
        mensagem = ''
    else:
        mensagem = 'Desculpa, ainda não temos postagens nessa sessão, volte mais tarde.'
    context = {
        "sessao" : sessaoAtual,
        "sessoes" : sessoes,
        "postagens" : postagens,
        "mensagem" : mensagem
    }
    return render(request, template, context)

def sobre(request):
    template = 'sobre.html'
    sessoes = Sessao.objects.all()
    context = {
        "sessoes": sessoes
    }
    return render(request, template, context)

def pesquisar(request):
    template = 'sessao.html'
    if request.GET:
        pesquisa = request.GET.get('pesquisa')
        postagens = Postagem.objects.filter(titulo__icontains=pesquisa, postar=True).order_by('-data')
        sessoes = Sessao.objects.all()
        if postagens:
            mensagem = ''
        else:
            mensagem = 'Desculpa, não temos postagens com o termo digitado. Tente pesquisa por outro termo.'
        context = {
            "sessoes" : sessoes,
            "mensagem" : mensagem,
            "postagens": postagens,
            "sessao": "Pesquisa"
        }
        return render(request, template, context)
    return render(request, template)

#pagina que irá renderizar as postagens
def postagem(request, slugSessao, slugPostagem):
    template = 'postagem.html'
    sessoes = Sessao.objects.all()
    postagem = Postagem.objects.get(slug=slugPostagem)
    try:
        comentarios = Comentario.objects.filter(postagem=postagem, aprovado=True)
    except:
        pass
    context = {
        "sessoes" : sessoes,
        "postagem" : postagem,
        "comentarios" : comentarios
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
