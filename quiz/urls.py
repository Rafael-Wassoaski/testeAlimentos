from django.urls import path, include
from . import views

app_name = "quiz"

urlpatterns = [
	path('newQuiz/<pk>/', views.criarQuiz, name = 'newQuiz'),
	path('answerQuiz/<pk>/', views.fazerQuiz, name = 'answerQuiz')

   
]