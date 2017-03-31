# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils import timezone
now = timezone.now()

@python_2_unicode_compatible
class Grado(models.Model):
	grado = models.CharField(max_length=15)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.grado

@python_2_unicode_compatible
class Seccion(models.Model):
	seccion = models.CharField(max_length=15)
	activo = models.BooleanField(default=True)
	def __str__(self):
		return self.seccion

@python_2_unicode_compatible
class GradoSeccion(models.Model):
	grado = models.ForeignKey(Grado)
	seccion = models.ForeignKey(Seccion)
	activo = models.BooleanField(default=True)

	class Meta:
		unique_together = ('grado', 'seccion')

	def _gradoseccion(self):
		return "%s %s" %(self.grado, self.seccion)

	gradoseccion = property(_gradoseccion)

	def __str__(self):
		return self.gradoseccion

@python_2_unicode_compatible
class Clase(models.Model):
	clase = models.CharField(max_length=30)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.clase

@python_2_unicode_compatible
class GradoClase(models.Model):
	grado = models.ForeignKey(Grado)
	clase = models.ForeignKey(Clase)

	class Meta:
		unique_together = ('grado', 'clase')

	def _clasegrado(self):
		return "%s %s" %(self.clase, self.grado)

	clasegrado = property(_clasegrado)

	def __str__(self):
		return self.clasegrado


class Anio(models.Model):
	inicio = models.DateField()
	fin = models.DateField()

	def __unicode__(self):
		return str(self.fin)

@python_2_unicode_compatible
class OfertaGrado(models.Model):
	gradoseccion = models.ForeignKey(GradoSeccion)
	anio = models.ForeignKey(Anio)
	capacidad = models.IntegerField()
	disponibles = models.IntegerField()

	class Meta:
		unique_together = ('gradoseccion', 'anio')

	def _gsa(self):
		return "%s %s" %(self.gradoseccion, self.anio)

	gsa = property(_gsa)

	def __str__(self):
		return self.gsa

@python_2_unicode_compatible
class Sexo(models.Model):
	sexo = models.CharField(max_length=9)

	def __str__(self):
		return self.sexo

@python_2_unicode_compatible
class EstadoClase(models.Model):
	estado = models.CharField(max_length=10)

	def __str__(self):
		return self.estado

@python_2_unicode_compatible
class EstadoAlumno(models.Model):
	estado = models.CharField(max_length=15)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.estado

@python_2_unicode_compatible
class Perfil(models.Model):
	numid = models.CharField(max_length=15)	
	direccion = models.CharField(max_length=100)
	telefono_f = models.CharField(max_length=9, blank=True, null=True)
	telefono_c = models.CharField(max_length=9, blank=True, null=True)
	usuario = models.OneToOneField(User, related_name='Perfil')
	sexo = models.ForeignKey(Sexo, null=True, blank=True)
	es_admin = models.BooleanField(default=False)
	es_secre = models.BooleanField(default=False)
	es_docente = models.BooleanField(default=False)
	es_tutor = models.BooleanField(default=False)

	def __str__(self):
		return self.usuario.username

@python_2_unicode_compatible
class Alumno(models.Model):
	numid = models.CharField(max_length=15)
	nombre = models.CharField(max_length=40)
	apellido = models.CharField(max_length=40)
	direccion = models.CharField(max_length=100)
	sexo = models.ForeignKey(Sexo, null=True, blank=True)
	telefono_f = models.CharField(max_length=9,)
	telefono_c = models.CharField(max_length=9)
	activo = models.BooleanField(default=True)
	correo = models.EmailField(blank=True, null=True)
	estadoalumno = models.ForeignKey(EstadoAlumno)


	def _nombrecompleto(self):
		return "%s %s" %(self.nombre, self.apellido)

	nombrecompleto = property(_nombrecompleto)

	def __str__(self):
		return self.nombrecompleto

@python_2_unicode_compatible
class EncargadoAlumno(models.Model):
	encargado = models.ForeignKey(User)
	alumno = models.ForeignKey(Alumno)

	class Meta:
		unique_together = ('encargado', 'alumno')

	def _encal(self):
		return "%s %s" %(self.encargado, self.alumno)

	encal = property(_encal)

	def __str__(self):
		return self.encal

class OfertaClase(models.Model):
	gradoclase = models.ForeignKey(GradoClase)
	ofertagrado = models.ForeignKey(OfertaGrado)
	docente = models.ForeignKey(User)

	class Meta:
		unique_together = ('gradoclase', 'ofertagrado', 'docente')

	def __unicode__(self):
		return str(self.gradoclase)


class Matricula(models.Model):
	alumno = models.ForeignKey(Alumno)
	ofertagrado = models.ForeignKey(OfertaGrado)
	fecha = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('alumno', 'ofertagrado')

	def __unicode__(self):
		return str(self.alumno)


class DetalleMatricula(models.Model):
	matricula = models.ForeignKey(Matricula)
	ofertaclase = models.ForeignKey(OfertaClase)
	nota1 = models.PositiveSmallIntegerField(default=0)
	nota2 = models.PositiveSmallIntegerField(default=0)
	nota3 = models.PositiveSmallIntegerField(default=0)
	nota4 = models.PositiveSmallIntegerField(default=0)
	estadoclase = models.ForeignKey(EstadoClase)

	class Meta:
		unique_together = ('matricula', 'ofertaclase')

	def _promedio(self):
		return ((self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4)

	promedio = property(_promedio)

	def __unicode__(self):
		return str(self.ofertaclase)


@python_2_unicode_compatible
class Configuracion(models.Model):
	nombre = models.CharField(max_length=15)
	direccion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=9)
	indice = models.IntegerField()
	logo =  models.ImageField(upload_to="media/logo")
	anioactual = models.ForeignKey(Anio)
	nombredirector = models.CharField(max_length=50, blank=True, null=True)
	telefonod = models.CharField(max_length=9, blank=True, null=True)

	def __str__(self):
		return self.nombre
