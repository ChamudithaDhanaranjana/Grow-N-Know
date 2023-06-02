from django.db import models

# Create your models here.
    
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