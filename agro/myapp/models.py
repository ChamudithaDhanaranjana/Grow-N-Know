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