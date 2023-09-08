from django.forms import ModelForm
from myapp.models import Category, Item, Order
from django.forms.widgets import CheckboxSelectMultiple

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