from django.shortcuts import render, redirect
from .models import Aula, Curso, cursoAluno
from .forms import FormularioAula, FormularioCurso
from contasAlunos.forms import CustomUserCreationForm
import noticias.views
from django.utils import timezone


from django.contrib.auth.decorators import user_passes_test, login_required
#usar login required aqui

@login_required
def entrarNoCurso(request, pkCurso):

	curso = Curso.objects.get(pk = pkCurso)

	try:
		cursoCadastro = cursoAluno.objects.get(aluno = request.user, curso = curso)
		return redirect("aulas:aulasList")
	except cursoAluno.DoesNotExist:
		
		cursoCadastro = cursoAluno()
		cursoCadastro.curso = curso
		cursoCadastro.aluno = request.user
		cursoCadastro.save()
		return redirect('aulas:aulasList')


def cursosList(request):
	cursos = Curso.objects.all()
	return render(request, 'html/aulas/cursosList.html', {'cursos':cursos, })

@user_passes_test(lambda u: u.is_superuser)
def criarNovaAula(request):
#	formAula = FormularioAula()
#	cursos = Curso.objects.all()

	if request.method == "POST":
		formAula = FormularioAula(request.POST, request.FILES)
		if formAula.is_valid():
			aula = formAula.save(commit = False)
			aula.autor = request.user
			aula.video = "https://www.youtube.com/embed/"+aula.video
			aula.data = timezone.now()
			curso = Curso.objects.get( pk = formAula.cleaned_data['curso'].pk)
			aula.idAula = curso.numAulas
			print(aula.idAula)
			curso.numAulas = curso.numAulas + 1
			curso.save()
			aula.save()
			return redirect('quiz:newQuiz', aula.pk)
	else:
		formAula = FormularioAula()
		formAula.fields["curso"].queryset = Curso.objects.all()
	return render(request, 'html/aulas/aulaForm.html', {'formAula':formAula, })




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
	aulas = Aula.objects.filter(data__lte=timezone.now()).order_by('-data')
	noticiasList = noticias.views.noticiasList()
	return render(request, 'index.html', {'aulas':aulas, 'noticias':noticiasList })



def aula(request, pk):
	aula = Aula.objects.get(pk = pk)
	curso = Curso.objects.get(pk = aula.curso.pk)
	try:
		aluno = cursoAluno.objects.get(aluno = request.user, curso = curso)
	except cursoAluno.DoesNotExist:
		return redirect("aulas:cursosList")

	
	
	if aluno.aula >= aula.idAula:	
		noticiasList = noticias.views.noticiasList()
		return render(request, 'html/aulas/aula.html', {'aula':aula, 'noticias':noticiasList })
	else:
		return redirect("aulas:aulasList")
	


def ajuda(request):
	noticiasList = noticias.views.noticiasList()
	return render(request, 'html/aulas/ajuda.html', {'noticias':noticiasList,})

def consultas(request):
	noticiasList = noticias.views.noticiasList()
	return render(request, 'html/aulas/consultas.html', {'noticias':noticiasList, })
