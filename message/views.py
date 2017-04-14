from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MensajeForm

from django.contrib.auth.models import User
from .models import *
def msg_index(request):
	form = MensajeForm(initial={'remitente': request.user, 'leido': False})
	users = User.objects.all()
	msjsr = Mensaje.objects.filter(destinatario= request.user).order_by('-fecha')
	total = msjsr.count()
	if request.user.Perfil.es_admin:
		return render(request, 'msg_index.html', {'msjsr':msjsr, 'users':users, 'total': total, 'form': form})
	elif request.user.Perfil.es_secre:
		return render(request, 'msg_index_secre.html', {'msjsr':msjsr, 'users':users, 'total': total, 'form': form})
	elif request.user.Perfil.es_docente:
		return render(request, 'msg_index_docente.html', {'msjsr':msjsr, 'users':users, 'total': total, 'form': form})
	elif request.user.Perfil.es_tutor:
		return render(request, 'msg_index_encargado.html', {'msjsr':msjsr, 'users':users, 'total': total, 'form': form})

def msg_enviados(request):
	form = MensajeForm(initial={'remitente': request.user, 'leido': False})
	users = User.objects.all()
	msjse = Mensaje.objects.filter(remitente= request.user).order_by('-fecha')
	msjsr = Mensaje.objects.filter(destinatario= request.user).order_by('-fecha')
	total = msjsr.count()
	if request.user.Perfil.es_admin:
		return render(request, 'msg_send.html' ,{'msjse':msjse, 'users':users,'total': total, 'form': form})
	elif request.user.Perfil.es_secre:
		return render(request, 'msg_send_secre.html' ,{'msjse':msjse, 'users':users,'total': total, 'form': form})
	elif request.user.Perfil.es_docente:
		return render(request, 'msg_send_docente.html' ,{'msjse':msjse, 'users':users,'total': total, 'form': form})
	elif request.user.Perfil.es_tutor:
		return render(request, 'msg_send_encargado.html' ,{'msjse':msjse, 'users':users,'total': total, 'form': form})

def msg_new(request):
	if request.method == 'POST':
		form = MensajeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/message/bandeja/')

@login_required()
def msg_delete(request, pk):
	msj = Mensaje.objects.get(pk=pk)
	try:
		msj.delete()
		return HttpResponseRedirect('/message/bandeja/')
	except Exception as e:
		return HttpResponse("")	

@login_required()
def msg_read(request, pk):
	msj = Mensaje.objects.get(pk=pk)
	try:
		msj.leido = True
		msj.save()
		return HttpResponse()
	except Exception as e:
		return HttpResponse()