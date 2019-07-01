from django.db import models
from aulas.models import Aula
from django.conf import settings
# Create your models here.







class Quiz(models.Model):
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	aula = models.ForeignKey(Aula, on_delete = models.CASCADE, related_name = 'Aula')


class Pergunta(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
	pergunta = models.TextField(blank = False);
	resposta = models.BooleanField(blank = False, default = False);

