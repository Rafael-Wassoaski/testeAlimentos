from django import forms
from .models import Noticia


class noticiaForm(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ('titulo', 'noticia', 'subtitulo', 'resumo', 'capa')
