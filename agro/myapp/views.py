from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from myapp.models import User, Problem, Feedback, Category, Item, Order, OrderItem
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import ItemForm, OrderForm
from django.forms.models import inlineformset_factory

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

# ..............................Order
class OrderCreateView(CreateView):
    template_name_suffix = "_create"
    model = Order
    fields = "__all__"
    success_url = "feedbacklistview"

class OrderListView(ListView):
    template_name_suffix = "_index"
    model = Order

def item(request, pk=None):
    model = Item.objects.get(pk=pk) if pk else Item()
    data = Item.objects.all()

    if request.POST.get('save'):
        form = ItemForm(request.POST, instance = model) 
        if form.is_valid():

            form.save()

            return redirect('/myapp/items')
    else:

        form = ItemForm(instance=model)

        if request.POST:
            model.delete()
            return redirect('/myapp/items')
        
    context = {'form':form, 'data':data}
    return render(request, 'myapp\item_create.html', context)

def order(request, pk=None):
    model = Order.objects.get(pk=pk) if pk else Order()
    data = Order.objects.all()

    OrderProductFormSet = inlineformset_factory(Order, OrderItem, fields='__all__', extra = 0 if pk else 1)

    if request.POST.get('save'):
        form = OrderForm(request.POST, instance = model) 
        formset = OrderProductFormSet(request.POST, instance=model)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('/myapp/orders')

    else:
        form = OrderForm(instance=model)
        formset = OrderProductFormSet(instance=model)

        if request.POST:
            model.delete()
            return redirect('/myapp/orders')

    context = {'form':form, 'data':data, 'formset':formset}
    return render(request, 'myapp\order_create.html', context)