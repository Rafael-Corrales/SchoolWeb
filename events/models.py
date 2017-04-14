from __future__ import unicode_literals

from django.db import models

class Evento(models.Model):
	titulo = models.CharField(max_length=40)
	descripcion = models.TextField()
	inicio = models.DateTimeField()
	fin = models.DateTimeField()
	fecha = models.DateTimeField(blank=True, null=True, auto_now_add=True)
