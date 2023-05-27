from django.shortcuts import render
from myapp.models import Problem
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

# Create your views here.

class ProblemCreateView(CreateView):

    template_name_suffix = "_create"
    model = Problem
    fields = "__all__"
    success_url = "problemlistview"

class ProblemListView(ListView):
    template_name_suffix = "_index"
    model = Problem
    #paginate_by = 3
   
class ProblemDetailView(DetailView):

    template_name_suffix = "_show"
    model = Problem

