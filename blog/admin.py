from django.contrib import admin
from .models import *

@admin.register(Sessao)
class SessaoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    prepopulated_fields = {
        'slug' : ('nome', )
    }

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    search_fields = ['titulo']
    prepopulated_fields = {
        'slug' : ('titulo', )
    }

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'aprovado', 'data']
    search_fields = ['data']
