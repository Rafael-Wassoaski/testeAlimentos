from django import forms
from .models import Aula, Curso

class FormularioAula(forms.ModelForm):
	class Meta:
		model = Aula
		fields = ('titulo', 'conteudo', 'resumo', 'video', 'ativo', 'capa', 'curso',)

	def __init__(self, *args, **kwargs):
		super(FormularioAula, self).__init__(*args, **kwargs)
		self.fields['titulo'].widget.attrs.update({'placeholder' : 'Título da aula'})
		self.fields['conteudo'].widget.attrs.update({'placeholder' : 'Descreva o conteúdo a ser apresentado nesta aula'})
		self.fields['resumo'].widget.attrs.update({'placeholder' : 'Insira um resumo desta aula para ser apresentado na página inicial'})
		self.fields['video'].widget.attrs.update({'placeholder' : 'Link do vídeo (Youtube)'})

class FormularioCurso(forms.ModelForm):
	class Meta:
		model = Curso
		fields = ('nome', 'descricao')

	def __init__(self, *args, **kwargs):
		super(FormularioCurso, self).__init__(*args, **kwargs)
		self.fields['nome'].widget.attrs.update({'placeholder' : 'Nome do curso'})
		self.fields['descricao'].widget.attrs.update({'placeholder' : 'Faça uma breve descrição para que os alunos saibam o conteúdo a ser apresentado no curso'})
