from django.db import models

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
        return self.title
    def __str__(self) :
        return self.description
    def __str__(self) :
        return self.link
    def __str__(self) :
        return self.image

class Item(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField(null=True)
    unit_price = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
