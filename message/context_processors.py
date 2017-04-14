#coding: utf8
from .models import Mensaje
def datos_globales(request):
	if request.user.is_authenticated():
		msj = Mensaje.objects.filter(destinatario= request.user)
		msjn = Mensaje.objects.filter(leido=False, destinatario =request.user)
		data = {}
		data['totmsj'] = msj.count()
		data['totmsjn'] = msjn.count()
		data['msjs'] = msj
	else:
		msj = Mensaje.objects.filter(leido=False)
		data = {}
		data['totmsj'] = msj.count()
	return data