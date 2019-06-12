from django import forms
from .models import Aula, Curso

class FormularioAula(forms.ModelForm):
	class Meta:
		model = Aula
		fields = ('titulo', 'conteudo', 'resumo', 'video', 'ativo', 'capa', 'curso',)


class FormularioCurso(forms.ModelForm):
	class Meta:
		model = Curso
		fields = ('nome',)
