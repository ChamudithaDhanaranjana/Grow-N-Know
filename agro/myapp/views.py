from audioop import reverse
from pyexpat.errors import messages

from django.views import View
from myapp.models import CartItem
from myapp.models import Solution
from myapp.models import Problem, Feedback, Category, Item, Order, OrderItem
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import CreateUserForm, ItemForm, OrderForm, SolutionForm
from django.forms.models import inlineformset_factory
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from myapp.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

# Create your views here.
def viewprofile(request):
    return TemplateResponse(request,'profile.html')

def homepage(request):
    return TemplateResponse(request,'home.html')

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
    model = Problem
    template_name_suffix = "_show"  # Make sure this matches your template naming convention

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        problem = self.object  # Get the problem object from the view
        solutions = Solution.objects.filter(problem=problem)  # Query solutions related to the problem
        context['solutions'] = solutions  # Add solutions to the context
        return context

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

# ..............................Order
class OrderCreateView(CreateView):
    template_name_suffix = "_create"
    model = Order
    fields = "__all__"
    success_url = "feedbacklistview"

class OrderListView(ListView):
    template_name_suffix = "_index"
    model = Order



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

def add_solution(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.problem = problem
            solution.save()
            return redirect('problem_detail', pk=problem_id)
    else:
        form = SolutionForm()

    return render(request, 'myapp/add_solution.html', {'form': form, 'problem': problem})

def problem_detail(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    solutions = problem.solutions.all()
    return render(request, 'myapp/problem_show.html', {'problem': problem, 'solutions': solutions})

class MyView(View):
    def get(self, request, pk):
        # pk contains the value extracted from the URL
        return redirect(reverse('problem_detail', kwargs={'pk': pk}))
    
class SolutionListView(ListView):
    model = Solution
    template_name = 'myapp/solution_list.html'
    context_object_name = 'solutions'

    def get_queryset(self):
        # Get the problem ID from the URL
        problem_id = self.kwargs['pk']  # Get the problem PK from URL
        return Solution.objects.filter(problem__pk=problem_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['problem_id'] = self.kwargs['problem_id']  # Pass problem ID to the template
        return context
class SolutionRemoveView(View):
    def post(self, request, pk):
        solution = Solution.objects.get(pk=pk)
        solution.delete()
        return redirect('problem_detail', pk=solution.problem.pk)

class SolutionUpdateView(View):
    def post(self, request, pk):
        solution = Solution.objects.get(pk=pk)
        # Handle form submission to update the solution
        if request.method == 'POST':
            # Update the solution fields as needed
            solution.description = request.POST.get('description')
            solution.save()
        return redirect('problem_detail', pk=solution.problem.pk)
    
from django.utils.safestring import mark_safe  

def activate(request, uidb64, token):
    return redirect('login')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html",{
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'http' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        message = mark_safe(f'Dear {user},  please go to your email <b>{to_email}</b> inbox and click on\
                    received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
        messages.success(request, message)
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

@user_passes_test(lambda u:not u.is_authenticated) 
def registeruser(request):
    form=CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))

            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('login')
        
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    return render(
        request=request,
        template_name="registrationform.html",
        context={"form":form}
    )            

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, item=item
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})

def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, user=request.user, item__pk=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, user=request.user, item__pk=item_id)
    cart_item.delete()
    return redirect('view_cart')
