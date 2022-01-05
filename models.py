from django.db import models
from django.db.models.fields import FloatField

 #Create your models here.
class Expense(models.Model):
  expense=models.CharField(max_length=100)
  amount=models.FloatField()

class Balance(models.Model):
    balance=models.FloatField()
