from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

def msg_index(request):
	return render(request, 'msg_index.html')

def msg_enviados(request):
	return render(request, 'msg_send.html')

def msg_new(request):
	return render(request, 'msg_new.html')