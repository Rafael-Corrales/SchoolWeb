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
	if request.user.Perfil.es_secre:
		alumnos = Alumno.objects.all()
		ofergra = OfertaGrado.objects.all()
		return render(request, 'new_enroll_s.html', {'alumnos':alumnos, 'ofergra': ofergra})
	else:
		return render(request, 'denegado.html')

@login_required()
def enroll_massive_s(request):
	if request.user.Perfil.es_secre:
		ga = OfertaGrado.objects.all()
		configuracion = Configuracion.objects.get(pk=1)
		anio = configuracion.anioactual
		ofergra = OfertaGrado.objects.filter(anio = anio)
		return render(request, 'massive_enroll_s.html', {'ga':ga, 'ofergra':ofergra})
	else:
		return render(request, 'denegado.html')

@login_required()
def enroll_massive_add_s(request):
		if request.method == 'POST':
			try:
				gradoM = request.POST.get('gradom')
				gradoA = request.POST.get('gradoa')
				gradoAnterior = OfertaGrado.objects.get(pk=gradoA)
				alumnos = Matricula.objects.filter(ofertagrado = gradoAnterior)
				go = OfertaGrado.objects.get(pk=gradoM)
				gc = GradoClase.objects.filter(grado = go.gradoseccion.grado)
				for alumno in alumnos:	
					a = Alumno.objects.get(pk=alumno.alumno.id)
					go.cupos = go.cupos - 1
					mat = Matricula(alumno = a, ofertagrado = go)	
					mat.save()
					go.save()
					for gradoc in gc:
						ec = EstadoClase.objects.get(pk=1)
						of = OfertaGrado.objects.get(ofertagrado = go, gradoclase = gradoc)
						dt = DetalleMatricula(ofertaclase = of, matricula = mat, estadoclase = ec)
						dt.save()
				return HttpResponseRedirect('/secretaria/enroll/massive/')
			except Exception as e:
				return HttpResponse(e)
	
@login_required()
def new_enroll(request):
	if request.user.Perfil.es_secre:
		configuracion = Configuracion.objects.get(pk=1)
		aniolectivo = configuracion.anioactual
		alumnos = Alumno.objects.all()
		ofergra = OfertaGrado.objects.filter(anio = aniolectivo)
		mat = Matricula.objects.filter(ofertagrado = ofergra).values_list('alumno_id', flat=True)
		alumnos = Alumno.objects.exclude(id_in = mat)
		return render(request, 'new_enroll.html_s', {'alumnos':alumnos, 'ofergra': ofergra})
	else:
		return render(request, 'denegado.html')

@login_required()	
def new_enroll_add_s(request):
	if request.method == 'POST':
		try:
			gradoOfertado = request.POST.get('ofergrado')
			alumnos = request.POST.getlist('alumno[]')
			go = OfertaGrado.objects.get(pk=gradoOfertado)
			gc = GradoClase.objects.filter(grado = go.gradoseccion.grado)
			for alumno in alumnos:	
				a = Alumno.objects.get(pk=alumno)
				go.cupos = go.cupos - 1
				mat = Matricula(alumno = a, ofertagrado = go)	
				mat.save()
				go.save()
				for gradoc in gc:
					ec = EstadoClase.objects.get(pk=1)
					of = OfertaGrado.objects.get(ofertagrado = go, gradoclase = gradoc)
					dt = DetalleMatricula(ofertaclase = of, matricula = mat, estadoclase = ec)
					dt.save()
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
