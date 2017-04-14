#coding: utf8
from .models import Configuracion
def datos_globales(request):
	configuracion = Configuracion.objects.get(pk=1)
	data = {}
	data['nombreescuela'] = configuracion.nombre
	data['direccionescuela'] = configuracion.direccion
	data['telefonoescuela'] = configuracion.telefono
	data['indice'] = configuracion.indice
	data['aniolectivo'] = configuracion.anioactual
	data['logo'] = configuracion.logo
	data['nombredirector'] = configuracion.nombredirector
	data['telefonodirector'] = configuracion.telefonod
	return data
