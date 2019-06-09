from django.shortcuts import render, redirect
from .models import Noticia
from .forms import noticiaForm
from django.utils import timezone

from django.contrib.auth.decorators import user_passes_test

# Create your views here.


@user_passes_test(lambda u: u.is_superuser)
def criarNoticia(request):
	formNoticia = noticiaForm()
	
	if request.method == "POST":
		formNoticia = noticiaForm(request.POST, request.FILES)
		if formNoticia.is_valid():
			noticia = formNoticia.save(commit = False)
			noticia.autor = request.user
			noticia.data = timezone.now()
			noticia.save()
			return redirect('aulas:aulasList')
	return render(request, 'html/noticias/noticiaForm.html', {'formNoticia':formNoticia,})

def noticiasList():
	noticias = Noticia.objects.filter(data__lte=timezone.now()).order_by('-data')[:5]
	return noticias

def noticiaRead(request, pk):
	noticia = Noticia.objects.get(pk = pk)
	return render(request, 'html/noticias/noticiaDetail.html', {'noticia':noticia,})


