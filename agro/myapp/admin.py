from django.contrib import admin
from myapp.models import User, Problem, Feedback, Item, Order, OrderItem

# Register your models here.
admin.site.register(User),
admin.site.register (Problem)
admin.site.register(Feedback)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)