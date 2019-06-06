from django.shortcuts import render, redirect
from .models import Aula
from .forms import FormularioAula

#usar login required aqui
def criarNovaAula(request):
	formAula = FormularioAula()
	if request.method == "POST":
		aulaForm = FormularioAula(request.POST)
		if aulaForm.is_valid():
			aula = aulaForm.save(commit = False)
			aula.autor = request.user
			aula.video = "https://www.youtube.com/embed/"+aula.video
			aula.save()
			return redirect('aulas:aulasList')
	return render(request, 'html/aulas/aulaForm.html', {'formAula':formAula})

def aulasList(request):
	aulas = Aula.objects.all()
	aulaaa = Aula.objects.get(pk=1)
	return render(request, 'index.html', {'aulas':aulas, 'aulaaa':aulaaa})

def aula(request, pk):
	aula = Aula.objects.get(pk = pk)
	if request.user.is_authenticated():
		return render(request, 'html/aulas/aula.html', {'aula':aula, 'aulaaa':aula})

	return render(request, 'html/aulas/aula.html', {'aula':aula})
