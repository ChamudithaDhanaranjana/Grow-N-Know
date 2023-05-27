from django.db import models

# Create your models here.
    
class Problem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.title + ""
    def __str__(self) :
        return self.description + ""