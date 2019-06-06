from django import forms
from .models import Aula, Curso

class FormularioAula(forms.ModelForm):
	class Meta:
		model = Aula
		fields = ('titulo', 'conteudo', 'video', 'ativo', 'capa')


class FormularioCurso(forms.ModelForm):
	class Meta:
		model = Curso
		fields = ('nome',)


