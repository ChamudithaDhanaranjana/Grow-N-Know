from asyncio import AbstractServer
from msilib.schema import SelfReg
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib.auth.models import User
    
class Problem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='problems')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title
    
class Solution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solutions')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='solutions')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solution for {self.problem.title}"
    
class Feedback(models.Model):
    email = models.CharField(max_length=150)
    comment = models.CharField(max_length=500,null=True)
    goal_achieved = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.email + ""
    def __str__(self) :
        return self.comment + ""
    def __str__(self) :
        return self.goal_achieved + ""


class Category(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500,null=True)
    link = models.CharField(max_length=100,null=True)
    image = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.title + ""
    def __str__(self) :
        return self.description + ""
    def __str__(self) :
        return self.link + ""

class Item(models.Model):
    name = models.CharField(max_length=150)
    available_quantity = models.IntegerField(null=True)
    unit_price = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    

class Order(models.Model):
    name = models.CharField(max_length=150)
    amount = models.IntegerField(null=True)
    item = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        created_at_local = timezone.localtime(self.created_at)
        created_at_local_formatted = created_at_local.strftime("%Y-%m-%d %H:%M:%S")
        return "%s %s" % (self.name, created_at_local_formatted)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "%s %s" % (self.order, self.item)
    
    class Meta:
        db_table ='myapp_order_item'
        unique_together = ('order', 'item',)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

