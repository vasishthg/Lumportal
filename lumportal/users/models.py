from django.db import models

# Create your models here.
class Oompa(models.Model):
    name= models.CharField(max_length=200, default="eheh")
    passw = models.CharField(max_length=200, default="eheh")
    level = models.IntegerField(default=1)
    salary =  models.IntegerField(default=1)
