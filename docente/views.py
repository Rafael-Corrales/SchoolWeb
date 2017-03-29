from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
# Create your views here.

@login_required()
def veralumnos(request):
	return render(request, 'veralumnos.html')

@login_required()
def ingresarnota(request):
	return render(request, 'ingresarnotas.html')

@login_required()
def vermisclases(request):
	return render(request, 'vermisclases.html')
