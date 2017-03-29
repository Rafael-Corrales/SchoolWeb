from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^veralumnos/$', views.veralumnos, name='veralumnos'),
	url(r'^vermisclases/$', views.vermisclases, name='vermisclases'),
	url(r'^ingresarnota/$', views.ingresarnota, name='ingresarnota'),

]