from django.shortcuts import render
from myapp.models import Problem
from django.views.generic.list import ListView

class ProblemListView(ListView):
    template_name_suffix = "_list"
    model = Problem
   
