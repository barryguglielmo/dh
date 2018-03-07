#main/views.py


from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'home.html')

def Final_Project(request):
    return render(request, 'Final_Project.html')
	
def home(request):
    return render(request, 'home.html')
	
def stacked_line(request):
    return render(request, 'graphs/stacked_line.html')

def doughnut(request):
    return render(request, 'graphs/doughnut.html')

def area(request):
    return render(request, 'graphs/area.html')

def about(request):
    return render(request, 'about.html')

def open_source_programming(request):
    return render(request, 'subjects/open_source_programming.html')
	
def next_gen_sequencing(request):
    return render(request, 'subjects/next_gen_sequencing.html')
	
def databases(request):
    return render(request, 'subjects/databases.html')
	
def web_based_tools(request):
    return render(request, 'subjects/web_based_tools.html')

def op_get_started(request):
    return render(request, 'subjects/open_source_html/op_get_started.html')
def r_tutorial_home(request):
    return render(request, 'subjects/open_source_html/r_tutorials/r_tutorial_home.html')
def python_tutorial_home(request):
    return render(request, 'subjects/open_source_html/python_tutorials/python_tutorial_home.html')	
def dojo_home(request):
    return render(request, 'subjects/open_source_html/dojo/dojo_home.html')
def the_buzz(request):
    return render(request, 'subjects/the_buzz.html')
	
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

