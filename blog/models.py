from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Sessao(models.Model):
    nome = models.CharField(max_length=125, null=False)
    slug = models.SlugField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Sessoes'

class Postagem(models.Model):
    titulo =  models.CharField(max_length=125, null=False)
    descricao = models.TextField(max_length=512, null=False)
    imagem = models.CharField(max_length=512, null=False)
    texto = RichTextUploadingField()
    slug = models.SlugField()
    data = models.DateField(auto_now=True)
    postar = models.BooleanField(default=False)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return (f'/{self.sessao.slug}/{self.slug}')

    class Meta:
        verbose_name_plural = 'Postagens'

class Comentario(models.Model):
    nome = models.CharField(max_length=125, null=False, editable=False)
    texto = models.TextField(max_length=255, null=False, editable=False)
    avaliacao = models.IntegerField(editable=False)
    aprovado = models.BooleanField(default=False)
    data = models.DateField(auto_now=True)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['data']
