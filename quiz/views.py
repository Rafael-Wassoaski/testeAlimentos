from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Quiz, Pergunta
from aulas.models import Aula, Curso, cursoAluno

from django.contrib.auth.decorators import user_passes_test

# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def criarQuiz(request, pk):

	if request.method == "POST":
		
		quiz = Quiz()
		listaPerguntas = [Pergunta(), Pergunta(), Pergunta(), Pergunta(), Pergunta()]


		listaPerguntas[0].pergunta = request.POST.get('pergunta1', 'Sem pergunta')
		if request.POST.getlist('resposta1') == ['True']:
			listaPerguntas[0].resposta = True
			

		listaPerguntas[1].pergunta = request.POST.get('pergunta2', 'Sem pergunta')
		if request.POST.getlist('resposta2')  == ['True']:
			listaPerguntas[1].resposta = True

		listaPerguntas[2].pergunta = request.POST.get('pergunta3', 'Sem pergunta')
		if request.POST.getlist('resposta3')  == ['True']:
			listaPerguntas[2].resposta = True

		listaPerguntas[3].pergunta = request.POST.get('pergunta4', 'Sem pergunta')
		if request.POST.getlist('resposta4')  == ['True']:
			listaPerguntas[3].resposta = True


		listaPerguntas[4].pergunta = request.POST.get('pergunta5', 'Sem pergunta')
		if request.POST.getlist('resposta5') == ['True']:
			listaPerguntas[4].resposta = True

		quiz.autor = request.user
		quiz.aula = Aula.objects.get(pk = pk)

		quiz.save()

		for pergunta in listaPerguntas:
			pergunta.quiz = quiz
			pergunta.save()

		return redirect('aulas:aulasList')
		

	return render(request, 'html/quiz/quizForm.html', {})

def fazerQuiz(request, pk):
	aulaPk = Aula.objects.get(pk = pk)
	quizDaAula = Quiz.objects.get(aula = aulaPk)
	perguntas = Pergunta.objects.filter(quiz = quizDaAula)

	if request.method == "POST":

		listaPerguntas = [
			request.POST.getlist('resposta1'), 
			request.POST.getlist('resposta2'),
			request.POST.getlist('resposta3'), 
			request.POST.getlist('resposta4'), 
			request.POST.getlist('resposta5')]

		print(listaPerguntas)
		pontos = 0;
		listaRespostas = []
		for  pergunta in listaPerguntas:
			
			if pergunta == ['True']:
				listaRespostas.append(True)
			else:
				listaRespostas.append(False)

		for (resposta, pergunta) in zip (listaRespostas, perguntas):
			
			if resposta == pergunta.resposta:
				pontos = pontos + 1


		if pontos >= 3:
			aula = Aula.objects.get(pk = pk)
			curso = Curso.objects.get(pk = aula.curso.pk)
			try:
				aluno = cursoAluno.objects.get(aluno = request.user, curso = curso)
				aluno.aula = aluno.aula + 1
				aluno.save()
				return redirect("aulas:aulasList")
			except cursoAluno.DoesNotExist:
				return redirect("aulas:aula",aula.pk )

	return render(request, 'html/quiz/responderQuiz.html', {'perguntas': perguntas})