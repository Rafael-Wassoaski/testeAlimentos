from django.db import models
from django.utils import timezone
from django.conf import settings


class Curso(models.Model):
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	nome = models.CharField(max_length = 100, default='', blank = False)
	numAulas = models.IntegerField(default = 0)
	descricao = models.TextField(default='', blank=False)

	def __str__(self):
		return '{}'.format(self.nome)

class Aula(models.Model):
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	titulo = models.CharField(max_length = 80, default='')
	data = models.DateTimeField(null = False)
	curso = models.ForeignKey(Curso, on_delete = models.CASCADE, blank = False, default = None, related_name = 'curso')
	conteudo = models.TextField(default='')
	resumo = models.CharField(max_length = 100, default = '', blank = True, null = True)
	video = models.CharField(max_length = 800, default='', blank = False, null = False)
	ativo = models.BooleanField(default=True)
	resumo = models.CharField(max_length = 1000, default='', blank = False)
	capa = models.ImageField(upload_to = 'images/', blank = True, default = None)
	idAula = models.IntegerField();

	def published_date(self):
		published_date = timezone.now()
		self.save()


class cursoAluno(models.Model):
	curso = models.ForeignKey(Curso, on_delete = models.CASCADE, related_name = 'cursoAluno')
	aluno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'aluno')
	aula = models.IntegerField(default = 0)

class Comentario(models.Model):
	aluno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='alunoComentario')
	aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name = 'aulaComentario')
	comentario = models.TextField()
	data = models.DateTimeField(null = False)

	def published_date(self):
		published_date = timezone.now()
		self.save()
