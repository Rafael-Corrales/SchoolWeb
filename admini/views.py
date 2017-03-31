from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import *

from django.contrib.auth.models import User
@login_required()
def index(request):
	return render(request, 'index.html')

@login_required()
def new_year(request):
	return render(request, 'new_year.html')

@login_required()
def new_year_add(request):
	if request.method == 'POST':
		inicio = request.POST.get('inicio')
		fin = request.POST.get('fin')
		a = Anio(inicio=inicio, fin=fin)
		a.save()
		return HttpResponseRedirect('/admini/year/new/')


@login_required()
def all_years(request):
	anio = Anio.objects.all()
	return render(request, 'all_years.html', {'anio':anio})

@login_required()
def new_grade(request):
	return render(request, 'new_grade.html')

@login_required()
def new_grade_add(request):
	if request.method == 'POST':
		try:
			grado = request.POST.get('grado')
			g = Grado(grado=grado)
			g.save()
			return HttpResponseResponse()
		except Exception as e:
			return HttpResponse(e)

@login_required()
def edit_grade(request, pk):
	if request.method == 'POST':
		grado = request.POST.get('grado')
		g = Grado.objects.get(pk=pk)
		g.grado = grado
		g.save()
		return HttpResponseRedirect('/admini/grade/all/')

@login_required()
def all_grades(request):
	grado = Grado.objects.all()
	total = Grado.objects.count()
	return render(request, 'all_grades.html', {'grado': grado, 'total': total})

@login_required()
def new_section(request):
	return render(request, 'new_section.html')

@login_required()
def new_section_add(request):
	if request.method == 'POST':
		try:
			seccion = request.POST.get('seccion')
			s = Seccion(seccion=seccion)
			s.save()
			return HttpResponseResponse()
		except Exception as e:
			return HttpResponse(e)


@login_required()
def edit_section(request, pk):
	if request.method == 'POST':
		seccion = request.POST.get('seccion')
		s = Seccion.objects.get(pk=pk)
		s.seccion = seccion
		s.save()
		return HttpResponseRedirect('/admini/grade/all/')

@login_required()
def all_sections(request):
	seccion = Seccion.objects.all()
	total = Seccion.objects.count()
	return render(request, 'all_sections.html', {'seccion':seccion, 'total': total})

@login_required()
def new_class(request):
	return render(request, 'new_class.html')

@login_required()
def new_class_add(request):
	if request.method == 'POST':
		try:
			clase = request.POST.get('clase')
			c = Clase(clase=clase)
			c.save()
			return HttpResponseResponse()
		except Exception as e:
			return HttpResponse(e)

@login_required()
def all_classes(request):
	clase = Clase.objects.all()
	return render(request, 'all_classes.html', {'clase': clase})

@login_required()
def edit_class(request, pk):
	if request.method == 'POST':
		clase = request.POST.get('clase')
		C = Clase.objects.get(pk=pk)
		C.clase = clase
		C.save()
		return HttpResponseRedirect('/admini/class/all/')
	
@login_required()
def new_grade_section(request):
	seccion = Seccion.objects.all()
	grado = Grado.objects.all()
	return render(request, 'new_grade_section.html', {'seccion': seccion, 'grado':grado})

@login_required()
def new_grade_section_add(request):
	if request.method == 'POST':
		try:
			grado = request.POST.get('grado')
			secciones = request.POST.getlist('seccion[]')
			g = Grado.objects.get(pk=grado)
			for seccion in secciones:	
				s = Seccion.objects.get(pk=seccion)
				GS = GradoSeccion(grado = g, seccion = s)	
				GS.save()
			return HttpResponseRedirect('/admini/grade_section/new/')
		except Exception as e:
			return HttpResponseRedirect('/admini/grade_section/new/')

@login_required()
def all_grades_section(request):
	return render(request, 'all_grades_section.html')

@login_required()
def new_grade_class(request):
	clase = Clase.objects.all()
	grado = Grado.objects.all()
	return render(request, 'new_grade_class.html', {'grado':grado, 'clase':clase})

@login_required()
def new_grade_class_add(request):
	if request.method == 'POST':
		try:
			grado = request.POST.get('grado')
			clases = request.POST.getlist('clase[]')
			g = Grado.objects.get(pk=grado)
			for clase in clases:	
				c = Clase.objects.get(pk=clase)
				GC = GradoClase(grado = g, clase=c)	
				GC.save()
			return HttpResponseRedirect('/admini/grade_class/new/')
		except Exception as e:
			return HttpResponseRedirect('/admini/grade_class/new/')

@login_required()
def offer_new_grade(request):
	anio = Anio.objects.all()
	gs = GradoSeccion.objects.all()
	return render(request, 'offer_new_grade.html', {'anio': anio, 'gs':gs})

@login_required()
def new_grade_offer_add(request):
	if request.method == 'POST':
		try:
			anio = request.POST.get('anio')
			cupos = request.POST.get('cupos')
			gradosecciones = request.POST.getlist('gradoseccion[]')
			a = Anio.objects.get(pk=anio)
			for gradoseccion in gradosecciones:	
				gs = GradoSeccion.objects.get(pk=gradoseccion)
				OG = OfertaGrado(anio = a,gradoseccion=gs, cupos=cupos)	
				OG.save()
			return HttpResponseRedirect('/admini/grade_offer/new/')
		except Exception as e:
			return HttpResponse(e)

@login_required()
def all_grades_offer(request):
	og = OfertaGrado.objects.all()
	return render(request, 'all_grades_offer.html', {'og':og})

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

