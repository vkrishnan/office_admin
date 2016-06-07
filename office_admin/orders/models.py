from django.db import models
from clients.models import Client
from django.utils import timezone

class Order(models.Model):
    STATUS_CHOICES = (
                        ('pending', 'Pending'),
                        ('accepted', 'Accepted'),
                        ('rejected', 'Rejected'),
                        ('completed', 'Completed'),
                     )
    user = models.ForeignKey(Client)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(  max_length=25,
                                choices = STATUS_CHOICES,
                                default='pending',
                            )

    def __unicode__(self):
        return self.name

class Transaction(models.Model):
    order = models.ForeignKey(Order)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.FloatField()
    payment = models.FloatField()
    comments = models.TextField(max_length=500)