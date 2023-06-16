from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    province = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    def __str__(self):
        return self.name + ""
    def __str__(self):
        return self.address + ""
    def __str__(self):
        return self.province + ""
    def __str__(self):
        return self.district + ""

    
class Problem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.title + ""
    def __str__(self) :
        return self.description + ""
    
    
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
    def __str__(self) :
        return self.image + ""

class Item(models.Model):
    name = models.CharField(max_length=150)
    available_quantity = models.IntegerField(null=True)
    unit_price = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name + ""

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