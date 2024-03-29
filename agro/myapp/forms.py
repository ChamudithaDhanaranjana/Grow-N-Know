from django.forms import ModelForm
from myapp.models import Solution
from myapp.models import Category, Item, Order
from django.forms.widgets import CheckboxSelectMultiple
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['items']
        fields = '__all__'
        widgets = {
            'items' : CheckboxSelectMultiple(),
        }

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['description']


class CreateUserForm(UserCreationForm):
    username = forms.CharField( widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Username",
        'size':'45',
    }) )

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Email",
        'size':'45',
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Password",
        'size':'45',
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Password",
        'size':'45',
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
        'username': forms.TextInput(attrs={'class': 'inputclass'}),
        'email': forms.TextInput(attrs={'class': 'inputclass'}),
        'password1': forms.PasswordInput(attrs={'class': 'inputclass'}),
        'password2': forms.PasswordInput(attrs={'class': 'inputclass'}),
    
    }