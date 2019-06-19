from django.contrib import admin
from .models import Aula, Curso, cursoAluno

# Register your models here.
admin.site.register(Aula)
admin.site.register(Curso)
admin.site.register(cursoAluno)


