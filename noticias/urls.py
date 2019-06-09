from django.urls import path, include
from . import views

app_name = "noticias"

urlpatterns = [

	path('criarNoticia/', views.criarNoticia, name = 'criarNoticia'),
	path('lerNoticia/<int:pk>/', views.noticiaRead, name = 'lerNoticia'),
	
   
]