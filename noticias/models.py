from django.db import models

# Create your models here.

class noticia(models.Model):
	 autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	 titulo = models.CharField(max_length = 100, default = '', blank = False)
	 noticia = models.TextField(blank = False);
	 subtitulo = models.CharField(max_length = 100, default = '', blank = True, null = True)
	 resumo = models.CharField(max_length = 100, default = '', blank = True, null = True)
