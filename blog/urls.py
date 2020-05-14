from django.urls import path
from django.conf.urls import url
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.sessao, name='sessao'),
    path('<slug:slugSessao>/<slug:slugPostagem>/', views.postagem, name='postagem'),
    path('<slug:slugSessao>/<slug:slugPostagem>/comentar/', views.comentar),
    path('sobre/', views.sobre, name='sobre')
]