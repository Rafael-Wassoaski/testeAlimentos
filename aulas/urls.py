from django.urls import path, include, re_path
from . import views

app_name = "aulas"

urlpatterns = [
    path('criarNovaAula/', views.criarNovaAula, name = 'criarNovaAula'),
    path('', views.aulasList, name = 'aulasList'),
    path('aula/<int:pk>/', views.aula, name = 'aula'),
    path('criarCurso/', views.criarCurso, name = 'criarCurso'),
    # path('', views.index, name='index'),
    # path('aula', views.aula, name='aula'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('consultas/', views.consultas, name='consultas'),
    # path('recuperarsenha', views.recuperarsenha, name='recuperarsenha'),
    path('cadastro/<int:pkCurso>', views.entrarNoCurso, name = 'entrarNoCurso'),
    path('cursosList/', views.cursosList, name = 'cursosList'),
    re_path(r'^pesquisa/?$', views.pesquisa, name='pesquisa'),
    path('comentar/<pkAula>/', views.comentar, name = 'comentar'),
    path('cursoAula/<pk>', views.cursoAula, name = 'cursoAula')

]
