from django.shortcuts import render, redirect
from .models import Aula, Curso, cursoAluno
from .forms import FormularioAula, FormularioCurso
from contasAlunos.forms import CustomUserCreationForm
import noticias.views
from django.utils import timezone
from django.contrib import messages



from django.contrib.auth.decorators import user_passes_test, login_required
#usar login required aqui

@login_required
def entrarNoCurso(request, pkCurso):

	curso = Curso.objects.get(pk = pkCurso)

	try:
		cursoCadastro = cursoAluno.objects.get(aluno = request.user, curso = curso)
		messages.error(request, 'Você já está cadastrado neste curso.')
		return redirect("aulas:aulasList")
	except cursoAluno.DoesNotExist:
		
		cursoCadastro = cursoAluno()
		cursoCadastro.curso = curso
		cursoCadastro.aluno = request.user
		cursoCadastro.save()
		messages.success(request, 'Você foi cadastrado no curso.')
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
			aula.video = aula.video.replace("watch?v=", "embed/")
			aula.data = timezone.now()
			curso = Curso.objects.get( pk = formAula.cleaned_data['curso'].pk)
			aula.idAula = curso.numAulas
			curso.numAulas = curso.numAulas + 1
			curso.save()
			aula.save()
			messages.success(request, 'Aula cadastrada com sucesso.')
			return redirect('quiz:newQuiz', aula.pk)
		else:
			messages.error(request, 'Não foi possível cadastrar aula.')
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
			messages.success(request, 'Curso criado com sucesso.')
			return redirect('aulas:aulasList')
		else:
			messages.error(request, 'Não foi possível criar o curso.')
	return render(request, 'html/aulas/cursoForm.html', {'formCurso':formCurso})




def aulasList(request):
	aulas = Aula.objects.filter(ativo = True,data__lte=timezone.now()).order_by('-data')
	noticiasList = noticias.views.noticiasList()
	return render(request, 'index.html', {'aulas':aulas, 'noticias':noticiasList })



def aula(request, pk):
	aula = Aula.objects.get(pk = pk)
	curso = Curso.objects.get(pk = aula.curso.pk)
	try:
		aluno = cursoAluno.objects.get(aluno = request.user, curso = curso)
	except cursoAluno.DoesNotExist:
		messages.error(request,'Você não está cadastrado no curso desta aula')
		return redirect("aulas:cursosList")

	
	
	if aluno.aula >= aula.idAula:	
		noticiasList = noticias.views.noticiasList()
		return render(request, 'html/aulas/aula.html', {'aula':aula, 'noticias':noticiasList, 'aluno': aluno })
	else:
		messages.error(request,'Você não tem acesso a esta aula')
		return redirect("aulas:aulasList")
	
def pesquisa(request):
	if request.method == "POST":
		try:
			aula = Aula.objects.filter(titulo__contains = request.POST.get['entrada_pesquisa'])
		except aula.DoesNotExist:
			messages.error(request,'Aula não encontrada')
			return redirect("aulas:aulasList")
		aula(request, aula.pk)


def ajuda(request):
	noticiasList = noticias.views.noticiasList()
	return render(request, 'html/aulas/ajuda.html', {'noticias':noticiasList,})

def consultas(request):
	noticiasList = noticias.views.noticiasList()
	return render(request, 'html/aulas/consultas.html', {'noticias':noticiasList, })
