from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index_encargado, name='index_encargado'),
	url(r'^vernotas/alumno/(?P<ida>\d+)/$', views.ver_notas_alumno, name='ver_notas_alumno'),
	url(r'^vermatricula/(?P<ida>\d+)/$', views.ver_matricula, name='ver_matricula'),
	# url(r'^verhistorial/$', views.ver_historial, name='ver_historial'),
	url(r'^veralumno/$', views.ver_alumnos, name='ver_alumnos'),
	url(r'^verdocente/(?P<ida>\d+)/$', views.ver_docente, name='ver_docente'),
	url(r'^verhistorial/alumno/$', views.ver_historial_alumno, name='ver_historial_alumno'),
	
]