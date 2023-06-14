from django.db import models

# Create your models here.

class coffee(models.Model):
    name=models.CharField( max_length=100)
    amount=models.IntegerField()
    paymentid=models.CharField(max_length=100)
    paid=models,models.BooleanField(default=False)
    def __str__(self) :
        return self.name
class sell(models.Model):
    chai=models.CharField(max_length=20)
    amount=models.IntegerField()
    