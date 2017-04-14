from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^bandeja/$', views.msg_index, name='msg_index'),
	url(r'^enviados/$', views.msg_enviados, name='msg_enviados'),
	url(r'^new/$', views.msg_new, name='msg_new'),
	url(r'^delete/(?P<pk>\d+)/$', views.msg_delete, name='msg_delete'),
	url(r'^read/(?P<pk>\d+)/$', views.msg_read, name='msg_read'),
]