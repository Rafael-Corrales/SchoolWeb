from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index_docente, name='index_docente'),
	url(r'^ver_alumnos/(?P<pk>\d+)/$', views.ver_alumnos, name='ver_alumnos'),
	url(r'^ver_misclases/$', views.ver_misclases, name='ver_misclases'),
	url(r'^ingresarnota/(?P<pk>\d+)/$', views.ingresarnota, name='ingresarnota'),
	url(r'^ingresarnota/save/$', views.ingresarnota_save, name='ingresarnota_save'),


]