from django.shortcuts import render
from django import forms
from myapp.models import User, Problem, Feedback, Category, Item
from .forms import CategoryForm, ItemForm
from django.forms.formsets import formset_factory
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

# Create your views here.
# ..............................User
class UserCreateView(CreateView):
    template_name_suffix = "_create"
    model = User
    fields = "__all__"
    success_url = "userlistview"

class UserListView(ListView):
    template_name_suffix = "_index"
    model = User
    paginate_by = 3

# ..............................Problem
class ProblemCreateView(CreateView):
    template_name_suffix = "_create"
    model = Problem
    fields = "__all__"
    success_url = "problemlistview"

class ProblemListView(ListView):
    template_name_suffix = "_index"
    model = Problem
   
class ProblemDetailView(DetailView):
    template_name_suffix = "_show"
    model = Problem

def problem_create(request):
    return render(request, 'myapp/problem_create.html')

# ..............................Feedback
class FeedbackListView(ListView):
    template_name_suffix = "_index"
    model = Feedback
    #paginate_by = 3

class FeedbackCreateView(CreateView):
    template_name_suffix = "_create"
    model = Feedback
    fields = "__all__"
    success_url = "feedbacklistview"

class FeedbackDetailView(DetailView):
    template_name_suffix = "_show"
    model = Feedback

# ..............................Category
class CategoryCreateView(CreateView):
    template_name_suffix = "_create"
    model = Category
    fields = "__all__"
    success_url = "categorylistview"

class CategoryListView(ListView):
    template_name_suffix = "_index"
    model = Category

# ..............................Item
class ItemCreateView(CreateView):
    template_name_suffix = "_create"
    model = Item
    fields = "__all__"
    success_url = "feedbacklistview"

class ItemListView(ListView):
    template_name_suffix = "_index"
    model = Item


# def category(request):
#     form = CategoryForm()
#     ItemFormSet = formset_factory(ItemForm)
#     formset = ItemFormSet()

#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         formset = ItemFormSet(request.POST)

#         if form.is_valid() and formset.is_valid():
#             category = form.save()
#             items = []

#             for inner_form in formset:
#                 title = inner_form.cleaned_data.get('title')
#                 description = inner_form.cleaned_data.get('description')
#                 link = inner_form.cleaned_data.get('link')
#                 image = inner_form.cleaned_data.get('image')
#                 item = Item(
#                     category=category,
#                     title=title,
#                     description=description,
#                     link=link,
#                     image=image
#                 )
#                 items.append(item)

#             Item.objects.bulk_create(items)

#     context={'form':form, 'formset':formset}
#     return render(request, 'category.html', context)

# def item(request):
#     form = ItemForm()
#     context={'form':form}
#     return render(request, 'item.html', context)