from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from admini.models import Sexo

@login_required()
def index_secretaria(request):
	return render(request, 'index_secretaria.html')

@login_required()
def new_enroll_s(request):
	return render(request, 'new_enroll_s.html')

@login_required()
def enroll_massive_s(request):
	return render(request, 'massive_enroll_s.html')

@login_required()
def all_enroll_s(request):
	return render(request, 'all_enroll_s.html')

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
