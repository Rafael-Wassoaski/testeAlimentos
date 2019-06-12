from django.db import models
from django.utils import timezone
from django.conf import settings


class Curso(models.Model):
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	nome = models.CharField(max_length = 100, default='', blank = False)

class Aula(models.Model):
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	titulo = models.CharField(max_length = 80, default='')
	data = models.DateTimeField(null = False)
	# ASSUNTOS = (
	# 	('ECA', 'ENTENDENDO A CONTAMINAÇÃO DOS ALIMENTOS'),
	# 	('AMA', 'AMBIENTE DE MANIPULAÇÃO E CUIDADOS COM ÁGUA'),
	# 	('MLV', 'MANUSEIO DO LIXO E CONTROLE DE VETORES E PRAGAS'),
	# 	('HIG', 'HIGIENIZAÇÃO'),
	# 	('MEV', 'MANIPULADORES E VISITANTES'),
	# 	('EDM', 'ETAPAS DA MANIPULAÇÃO'),
	# 	('DOC', 'DOCUMENTAÇÃO'),

	# 	)
	# assuntos = models.CharField(max_length = 3, choices = ASSUNTOS, default='')
	curso = models.ForeignKey(Curso, on_delete = models.CASCADE, blank = False, default = None, related_name = 'curso')
	conteudo = models.TextField(default='')
	resumo = models.CharField(max_length = 100, default = '', blank = True, null = True)
	video = models.CharField(max_length = 800, default='', blank = False)
	ativo = models.BooleanField(default=True)
	resumo = models.CharField(max_length = 1000, default='', blank = False)
	capa = models.ImageField(upload_to = 'images/', blank = True, default = None)

	def published_date(self):
		published_date = timezone.now()
		self.save()


class Comentario(models.Model):
	#criar classe aluno
	aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
	comentario = models.TextField()

	def published_date(self):
		published_date = timezone.now()
		self.save()
