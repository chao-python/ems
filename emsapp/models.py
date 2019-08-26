from django.db import models

# Create your models here.


class Employeelist(models.Model):
    headpic = models.ImageField(upload_to='pics', null=True)
    name = models.CharField(max_length=20)
    salary = models.IntegerField()
    age = models.SmallIntegerField()
    operation = models.CharField(max_length=20)

