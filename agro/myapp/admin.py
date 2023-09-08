from django.contrib import admin
from myapp.models import Problem, Feedback, Item, Order, OrderItem

admin.site.register (Problem)
admin.site.register(Feedback)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)