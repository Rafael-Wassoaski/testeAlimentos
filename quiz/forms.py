from django import forms
from .models import Pergunta

class Formulariopergunta(forms.ModelForm):
	class Meta:
		model = Pergunta
		fields = ('pergunta', 'resposta', )


