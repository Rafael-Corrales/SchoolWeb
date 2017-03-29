from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .models import Sexo, Clase, Grado, Seccion
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.contrib.auth.models import User
@login_required()
def index(request):
	return render(request, 'index.html')

@login_required()
def new_year(request):
	return render(request, 'new_year.html')

@login_required()
def all_years(request):
	return render(request, 'all_years.html')

@login_required()
def new_grade(request):
	return render(request, 'new_grade.html')

@login_required()
def all_grades(request):
	grado = Grado.objects.all()
	total = Grado.objects.count()
	return render(request, 'all_grades.html', {'grado': grado, 'total': total})

@login_required()
def new_section(request):
	return render(request, 'new_section.html')

@login_required()
def all_sections(request):
	seccion = Seccion.objects.all()
	total = Seccion.objects.count()
	return render(request, 'all_sections.html', {'seccion':seccion, 'total': total})

@login_required()
def new_class(request):
	return render(request, 'new_class.html')

@login_required()
def all_classes(request):
	clase = Clase.objects.all()
	total = Clase.objects.count()
	return render(request, 'all_classes.html', {'clase': clase, 'total': total})

class edit_class(TemplateView):
	def get(self, request, *args, **kwargs):
		id_c = request.GET['id']
		clase = Clase.objects.filter(id=id_c)
		data = serializers.serialize('json', clase, fields=('clase'))
		return HttpResponse(data, mimetype='application/json')

@login_required()
def new_grade_section(request):
	return render(request, 'new_grade_section.html')

@login_required()
def all_grades_section(request):
	return render(request, 'all_grades_section.html')

@login_required()
def new_grade_class(request):
	return render(request, 'new_grade_class.html')

@login_required()
def offer_new_grade(request):
	return render(request, 'offer_new_grade.html')

@login_required()
def all_grades_offer(request):
	return render(request, 'all_grades_offer.html')

@login_required()
def offer_new_class(request):
	return render(request, 'offer_new_class.html')

@login_required()
def all_classes_offer(request):
	return render(request, 'all_classes_offer.html')

@login_required()
def new_enroll(request):
	return render(request, 'new_enroll.html')

@login_required()
def enroll_massive(request):
	return render(request, 'massive_enroll.html')

@login_required()
def all_enroll(request):
	return render(request, 'all_enroll.html')

@login_required()
def new_student(request):
	sexo = Sexo.objects.all()
	return render(request, 'new_student.html', {'sexo': sexo})

@login_required()
def all_students(request):
	return render(request, 'all_students.html')

@login_required()
def new_workposition(request):
	return render(request, 'new_workposition.html')

@login_required()
def all_workpositions(request):
	return render(request, 'all_workpositions.html')

@login_required()
def new_employee(request):
	sexo = Sexo.objects.all()
	return render(request, 'new_employee.html', {'sexo': sexo})

@login_required()
def all_employees(request):
	return render(request, 'all_employees.html')

@login_required()
def new_user(request):
	return render(request, 'new_user.html')

@login_required()
def all_users(request):
	return render(request, 'all_users.html')

@login_required()
def new_tutor(request):
	sexo = Sexo.objects.all()
	return render(request, 'new_tutor.html', {'sexo': sexo})

@login_required()
def all_tutors(request):
	return render(request, 'all_tutors.html')

@login_required()
def settings(request):
	return render(request, 'settings.html')

@login_required()
def events(request):
	return render(request, 'events.html')

