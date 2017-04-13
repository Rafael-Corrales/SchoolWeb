from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from admini.models import *

from django.contrib.auth.models import User
# Create your views here.

@login_required()
def index_docente(request):
	if request.user.Perfil.es_docente:
		return render(request, 'index_docente.html')
	else:
		return render(request, 'denegado.html')



@login_required()
def ingresarnota(request, pk):
	detm = []
	if request.user.Perfil.es_docente:
		of = OfertaClase.objects.get(pk=pk)
		mat = Matricula.objects.filter(ofertagrado=of.ofertagrado)
		for matri in mat:
			detm2 = DetalleMatricula.objects.filter(matricula=matri)
			detm.append(detm2)
			
		return render(request, 'ingresarnotas.html', {'detm': detm, 'of': of})
		#return HttpResponse(detm2)
	else:
		return render(request, 'denegado.html')


@login_required()
def ver_misclases(request):
	if request.user.Perfil.es_docente:
		misclases = OfertaClase.objects.filter(docente=request.user)
		return render(request, 'ver_misclases.html', {'misclases': misclases})
	else:
		return render(request, 'denegado.html')

@login_required()
def ver_alumnos(request, pk):
	if request.user.Perfil.es_docente:
		of = OfertaClase.objects.get(pk=pk)
		mat = Matricula.objects.filter(ofertagrado=of.ofertagrado)


		return render(request, 'ver_alumnos.html', {'mat': mat, 'of': of})
	else:
		return render(request, 'denegado.html')