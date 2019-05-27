from django.urls import path

from . import views

app_name = "contas"
urlpatterns = [
    path('cadastrar/', views.Cadastrar.as_view(), name='cadastrar'),
]