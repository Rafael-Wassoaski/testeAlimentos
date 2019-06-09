from django.shortcuts import render, redirect
from .models import Aula, Curso
from .forms import FormularioAula, FormularioCurso
from contasAlunos.forms import CustomUserCreationForm
import noticias.views

from django.contrib.auth.decorators import user_passes_test
#usar login required aqui


@user_passes_test(lambda u: u.is_superuser)
def criarNovaAula(request):
	formAula = FormularioAula()
	cursos = Curso.objects.all()

	if request.method == "POST":
		aulaForm = FormularioAula(request.POST, request.FILES)
		if aulaForm.is_valid():
			aula = aulaForm.save(commit = False)
			aula.autor = request.user
			aula.video = "https://www.youtube.com/embed/"+aula.video
			# aula.curso = Curso.objects.get(pk=r)
			print(aulaForm.cleaned_data['cursoId'])
			aula.save()
			return redirect('aulas:aulasList')
	return render(request, 'html/aulas/aulaForm.html', {'formAula':formAula, 'cursos': cursos})




@user_passes_test(lambda u: u.is_superuser)
def criarCurso(request):
	formCurso = FormularioCurso()
	if request.method == "POST":
		cursoForm = FormularioCurso(request.POST)
		if cursoForm.is_valid():
			curso = cursoForm.save(commit = False)
			curso.autor = request.user
			curso.save()
			return redirect('aulas:aulasList')
	return render(request, 'html/aulas/cursoForm.html', {'formCurso':formCurso})




def aulasList(request):
	aulas = Aula.objects.all()
	noticiasList = noticias.views.noticiasList()
	print(noticiasList)
	return render(request, 'index.html', {'aulas':aulas, 'noticias':noticiasList })




def aula(request, pk):
	aula = Aula.objects.get(pk = pk)
	return render(request, 'html/aulas/aula.html', {'aula':aula})


