from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
	remitente = models.ForeignKey(User, related_name='fromuser')
	asunto =  models.CharField(max_length=50)
	contenido = models.TextField()
	destinatario = models.ForeignKey(User, related_name='touser')
	leido = models.BooleanField(default=False)
	archivo = models.FileField(upload_to="media/message", blank=True,null=True)
	fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __unicode__(self):
		return unicode(self.asunto)
