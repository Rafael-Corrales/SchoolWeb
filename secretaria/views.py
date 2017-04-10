from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

from admini.models import *

@login_required()
def index_secretaria(request):
	return render(request, 'index_secretaria.html')

@login_required()
def new_enroll_s(request):
	alumnos = Alumno.objects.all()
	ofergra = OfertaGrado.objects.all()
	return render(request, 'new_enroll_s.html', {'alumnos':alumnos, 'ofergra': ofergra})

@login_required()
def enroll_massive_s(request):
	return render(request, 'massive_enroll_s.html')

@login_required()
def all_enroll_s(request):
	m = Matricula.objects.all()
	return render(request, 'all_enroll_s.html', {'m':m})


def new_enroll_add_s(request):
	if request.method == 'POST':
		try:
			gradoOfertado = request.POST.get('ofergrado')
			alumnos = request.POST.getlist('alumno[]')
			go = OfertaGrado.objects.get(pk=gradoOfertado)
			#gs = GradoSeccion.objects.get(pk= go.GradoSeccion)
			#g = Grado.objects.get(pk=gs.grado)
			for alumno in alumnos:	
				a = Alumno.objects.get(pk=alumno)
				go.cupos = go.cupos - 1
				mat = Matricula(alumno = a, ofertagrado = go)	
				i = mat.save()

			return HttpResponseRedirect('/secretaria/enroll/new/')
		except Exception as e:
			return HttpResponse(e)

@login_required()
def new_student_s(request):
	sexo = Sexo.objects.all()
	return render(request, 'new_student_s.html', {'sexo': sexo})

@login_required()
def all_students_s(request):
	return render(request, 'all_students_s.html')

@login_required()
def new_tutor_s(request):
	sexo = Sexo.objects.all()
	return render(request, 'new_tutor_s.html', {'sexo': sexo})

@login_required()
def all_tutors_s(request):
	return render(request, 'all_tutors_s.html')
