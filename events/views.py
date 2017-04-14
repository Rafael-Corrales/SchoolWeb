from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from .models import Evento
from .forms import EventoForm
@login_required()
def events(request):
	eventos = Evento.objects.all()
	if request.user.Perfil.es_admin:
		return render(request, 'events.html', {'eventos':eventos})
	elif request.user.Perfil.es_docente:
		return render(request, 'events_docente.html', {'eventos':eventos})
	elif request.user.Perfil.es_tutor:
		return render(request, 'events_encargado.html', {'eventos':eventos})
	elif request.user.Perfil.es_secre:
		return render(request, 'events_secre.html', {'eventos':eventos})

@login_required()
def events_all(request):
	eventos = Evento.objects.all().order_by('-fecha')
	if request.user.Perfil.es_admin:
		return render(request, 'events_all.html', {'eventos':eventos})
	elif request.user.Perfil.es_docente:
		return render(request, 'events_all_docente.html', {'eventos':eventos})
	elif request.user.Perfil.es_tutor:
		return render(request, 'events_all_encargado.html', {'eventos':eventos})
	elif request.user.Perfil.es_secre:
		return render(request, 'events_all_secre.html', {'eventos':eventos})

@login_required()
def events_add(request):
	if request.method == 'POST':
		titulo = request.POST.get('titulo')
		descripcion = request.POST.get('descripcion')
		iniciofecha = request.POST.get('iniciofecha')
		finfecha = request.POST.get('finfecha')
		iniciohora = request.POST.get('iniciohora')
		finhora = request.POST.get('finhora')
		inicio = iniciofecha + " " + iniciohora
		fin = finfecha + " " + finhora
		e = Evento(inicio=inicio, fin=fin, titulo= titulo, descripcion = descripcion)
		e.save()
		return HttpResponseRedirect('/events/')

@login_required()
def events_add_2(request):
	if request.method == 'POST':
		titulo = request.POST.get('titulo')
		descripcion = request.POST.get('descripcion')
		iniciofecha = request.POST.get('iniciofecha')
		finfecha = request.POST.get('finfecha')
		iniciohora = request.POST.get('iniciohora')
		finhora = request.POST.get('finhora')
		inicio = iniciofecha + " " + iniciohora
		fin = finfecha + " " + finhora
		e = Evento(inicio=inicio, fin=fin, titulo= titulo, descripcion = descripcion)
		e.save()
		return HttpResponseRedirect('/events/all/')

@login_required()
def events_delete(request, pk):
	evento = Evento.objects.get(pk=pk)
	evento.delete()
	return HttpResponseRedirect('/events/all/')

@login_required()
def events_edit(request, pk):
	if request.method == 'POST':
		titulo = request.POST.get('evento')
		descripcion = request.POST.get('descripcion')
		iniciofecha = request.POST.get('iniciofecha')
		finfecha = request.POST.get('finfecha')
		iniciohora = request.POST.get('iniciohora')
		finhora = request.POST.get('finhora')
		inicio = iniciofecha + " " + iniciohora
		fin = finfecha + " " + finhora
		eventos = Evento.objects.get(pk=pk)
		eventos.titulo = titulo
		eventos.descripcion = descripcion
		eventos.inicio = inicio
		eventos.fin = fin
		eventos.save()
		return HttpResponseRedirect('/events/all/')