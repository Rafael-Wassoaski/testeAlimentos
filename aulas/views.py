from django.shortcuts import render, redirect
from .models import Aula, Curso, cursoAluno, Comentario
from .forms import FormularioAula, FormularioCurso,FormularioComentario
from contasAlunos.forms import CustomUserCreationForm
import noticias.views
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail



from django.contrib.auth.decorators import user_passes_test, login_required
#usar login required aqui


@login_required
def comentar(request, pkAula):
	if request.method == "POST":

		comentario = Comentario()

		comentario.aula = Aula.objects.get(pk = pkAula)
		comentario.aluno = request.user
		comentario.data = timezone.now()
		comentario.comentario = request.POST.get('comentario')
		comentario.save()
		messages.success(request, 'Comentario registrado com sucesso')
		return redirect('aulas:aula', pkAula)



	

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
			try:
				alunos = cursoAluno.objects.filter(curso = curso)
			except cursoAluno.DoesNotExist:
				return redirect('quiz:newQuiz', aula.pk)

			for aluno in alunos:	
				print("enviando")
				send_mail('Novo aula BPF IFSC', 'Olá {}, uma nova aula foi cadastrada no curso de {}: {}'.format(aluno.aluno.username, curso.nome, aula.titulo), ['bpf.ifsc@gmail.com'], [aluno.aluno.email])



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
		comentarios = Comentario.objects.filter(aula = aula)
		return render(request, 'html/aulas/aula.html', {'aula':aula, 'noticias':noticiasList, 'aluno': aluno, 'comentarios':comentarios })
	else:
		messages.error(request,'Você não tem acesso a esta aula')
		return redirect("aulas:aulasList")
	
def pesquisa(request):
	if request.method == "GET":
		
		aulas= Aula.objects.filter(titulo__contains = request.GET.get('entrada_pesquisa', None))
		
		if not aulas:
			messages.error(request,'Aula não encontrada')
			return render(request, 'html/aulas/semAula.html', {'busca': request.GET.get('entrada_pesquisa', None)})
		else:
			return render(request, 'index.html', {'aulas':aulas, })


def ajuda(request):
	noticiasList = noticias.views.noticiasList()
	return render(request, 'html/aulas/ajuda.html', {'noticias':noticiasList,})

def consultas(request):
	
	noticiasList = None
	aulasList = None
	curso = None
	if request.GET.get('consulta') == 'aulas':
		aulasList = Aula.objects.all()
	if request.GET.get('consulta') == 'noticias':
		noticiasList = noticias.views.noticiasList()
	if request.GET.get('consulta') == 'cursos':
		curso = Curso.objects.all()
	
	return render(request, 'html/aulas/consultas.html', {'noticias':noticiasList, 'aulas':aulasList, 'cursos':curso})



def cursoAula(request, pk):
	try:
		cursoPk = Curso.objects.get(pk = pk)
	except Curso.DoesNotExist:
		messages.error(request, 'Curso inexitente')
		return redirect('aulas:consultas')

	aulasList = Aula.objects.filter (curso = cursoPk)
	return render(request, 'html/aulas/consultasAulasCurso.html', {'aulas': aulasList, 'curso':cursoPk})