from django.db import models
from django.urls import reverse

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=40,null=True)
    father_name = models.CharField(max_length=40,null=True)
    caste = models.CharField(max_length=30,null=True)
    mobile = models.CharField(max_length=12,null=True)
    aadhaar = models.CharField(max_length=12,null=True)
    items = models.CharField(default='0',max_length=20,null=True)
    lending_amount = models.CharField(default='0',max_length=40,null=True)
    total_intrest = models.CharField(default='0',max_length=40,null=True)
    date = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse('customers')

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=40,null=True)
    item_id = models.CharField(max_length=40,null=True)
    weight = models.CharField(max_length=40,null=True)
    date = models.DateTimeField(auto_now_add=True)
    lending_amount = models.CharField(max_length=40,null=True)
    intrest = models.CharField(max_length=10,null=True)
    remarks = models.TextField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('items', kwargs={'pk': self.customer.pk})

    def __str__(self):
        return self.name