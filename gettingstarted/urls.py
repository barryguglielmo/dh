#gettingstarted/urls.py
from django.conf.urls import include, url


from django.contrib import admin
admin.autodiscover()

import main.views

urlpatterns = [
    url(r'^$', main.views.index, name='index'),
    url(r'^db', main.views.db, name='db'),
	url(r'^Final_Project/', main.views.Final_Project, name = 'Final_Project'),
	url(r'^home/', main.views.home, name = 'home'),
	url(r'^stacked_line/', main.views.stacked_line, name = 'stacked_line'),
	url(r'^doughnut/', main.views.doughnut, name = 'doughnut'),
	url(r'^area/', main.views.area, name = 'area'),
	url(r'^about/', main.views.about, name = 'about'),
	url(r'^open_source_programming/', main.views.open_source_programming, name = 'open_source_programming'),
	url(r'^next_gen_sequencing/', main.views.next_gen_sequencing, name = 'next_gen_sequencing'),
	url(r'^databases/', main.views.databases, name = 'databases'),
	url(r'^web_based_tools/', main.views.web_based_tools, name = 'web_based_tools'),
	url(r'^op_get_started/', main.views.op_get_started, name = 'op_get_started'),
	url(r'^r_tutorial_home/', main.views.r_tutorial_home, name = 'r_tutorial_home'),
	url(r'^python_tutorial_home/', main.views.python_tutorial_home, name = 'python_tutorial_home'),
	url(r'^dojo_home/', main.views.dojo_home, name = 'dojo_home'),
	url(r'^the_buzz/', main.views.the_buzz, name = 'the_buzz'),
	]
