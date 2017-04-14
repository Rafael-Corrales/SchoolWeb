from django.conf.urls import url
from . import views
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
	url(r'^$', views.events, name='events'),
	url(r'^all/$', views.events_all, name='events_all'),
	url(r'^add/$', views.events_add, name='events_add'),
	url(r'^add/2/$', views.events_add_2, name='events_add_2'),
	url(r'^delete/(?P<pk>\d+)/$', views.events_delete, name='events_delete'),
	url(r'^edit/(?P<pk>\d+)/$', views.events_edit, name='events_edit'),
]