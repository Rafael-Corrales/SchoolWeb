from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index_secretaria, name='index_secretaria'),
	url(r'^enroll/new/$', views.new_enroll_s, name='new_enroll_s'),
	url(r'^enroll/massive/$', views.enroll_massive_s, name='enroll_massive_s'),
	url(r'^enroll/all/$', views.all_enroll_s, name='all_enroll_s'),
	url(r'^enroll/new/add/$', views.new_enroll_add_s, name='new_enroll_add_s'),
	url(r'^student/new/$', views.new_student_s, name='new_student_s'),
	url(r'^student/all/$', views.all_students_s, name='all_students_s'),
	url(r'^tutor/all/$', views.all_tutors_s, name='all_tutors_s'),
	url(r'^tutor/new/$', views.new_tutor_s, name='new_tutor_s'),

]