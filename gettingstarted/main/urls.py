#main/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Final_Project/', views.Final_Project, name='Final_Project'),
	url(r'^home/', views.home, name='home'),
	url(r'^stacked_line/', views.stacked_line, name='stacked_line'),
	url(r'^area/', views.area, name='area'),
	url(r'^about/', views.about, name='about'),
	url(r'^open_source_programming/', views.open_source_programming, name='open_source_programming'),
	url(r'^next_gen_sequencing/', views.next_gen_sequencing, name='next_gen_sequencing'),
	url(r'^databases/', views.databases, name='databases'),
	url(r'^web_based_tools/', views.web_based_tools, name='web_based_tools'),
	url(r'^op_get_started/', views.op_get_started, name='op_get_started'),
	url(r'^r_tutorial_home/', views.r_tutorial_home, name = 'r_tutorial_home'),
	url(r'^python_tutorial_home/', views.python_tutorial_home, name = 'python_tutorial_home'),
	url(r'^dojo_home/', views.dojo_home, name = 'dojo_home'),
	url(r'^the_buzz/', views.the_buzz, name = 'the_buzz'),

	]
