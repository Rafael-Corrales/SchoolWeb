from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^year/new/$', views.new_year, name='new_year'),
	url(r'^year/new/add/$', views.new_year_add, name='new_year_add'),
	url(r'^year/all/$', views.all_years, name='all_years'),
	url(r'^grade/new/$', views.new_grade, name='new_grade'),
	url(r'^grade/new/add/$', views.new_grade_add, name='new_grade_add'),
	url(r'^grade/edit/(?P<pk>\d+)/$', views.edit_grade, name='edit_grade'),
	url(r'^grade/all/$', views.all_grades, name='all_grades'),
	url(r'^section/new/$', views.new_section, name='new_section'),
	url(r'^section/new/add/$', views.new_section_add, name='new_section_add'),
	url(r'^section/edit/(?P<pk>\d+)/$', views.edit_section, name='edit_section'),
	url(r'^section/all/$', views.all_sections, name='all_sections'),
	url(r'^class/new/$', views.new_class, name='new_class'),
	url(r'^class/new/add/$', views.new_class_add, name='new_class_add'),
	url(r'^class/all/$', views.all_classes, name='all_classes'),
	url(r'^class/edit/(?P<pk>\d+)/$', views.edit_class, name='edit_class'),
	url(r'^grade_section/new/$', views.new_grade_section, name='new_grade_section'),
	url(r'^grade_section/new/add/$', views.new_grade_section_add, name='new_grade_section_add'),
	url(r'^grade_section/all/$', views.all_grades_section, name='all_grades_section'),
	url(r'^grade_class/new/$', views.new_grade_class, name='new_grade_class'),
	url(r'^grade_class/new/add/$', views.new_grade_class_add, name='new_grade_class_add'),
	url(r'^grade_offer/new/$', views.offer_new_grade, name='offer_new_grade'),
	url(r'^grade_offer/new/add/$', views.new_grade_offer_add, name='new_grade_offer_add'),
	url(r'^grade_offer/all/$', views.all_grades_offer, name='all_grades_offer'),
	url(r'^class_offer/new/$', views.offer_new_class, name='offer_new_class'),
	url(r'^class_offer/all/$', views.all_classes_offer, name='all_classes_offer'),
	url(r'^enroll/new/$', views.new_enroll, name='new_enroll'),
	url(r'^enroll/massive/$', views.enroll_massive, name='enroll_massive'),
	url(r'^enroll/all/$', views.all_enroll, name='all_enroll'),
	url(r'^enroll/new/add/$', views.new_enroll_add, name='new_enroll_add'),
	url(r'^student/new/$', views.new_student, name='new_student'),
	url(r'^student/all/$', views.all_students, name='all_students'),
	url(r'^workposition/new/$', views.new_workposition, name='new_workposition'),
	url(r'^workposition/all/$', views.all_workpositions, name='all_workpositions'),
	url(r'^employee/new/$', views.new_employee, name='new_employee'),
	url(r'^employee/all/$', views.all_employees, name='all_employees'),
	url(r'^user/new/$', views.new_user, name='new_user'),
	url(r'^user/all/$', views.all_users, name='all_users'),
	url(r'^tutor/all/$', views.all_tutors, name='all_tutors'),
	url(r'^tutor/new/$', views.new_tutor, name='new_tutor'),
	url(r'^settings/$', views.settings, name='settings'),
	url(r'^events/$', views.events, name='events'),

]