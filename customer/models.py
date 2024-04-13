from django.db import models
from agency.models import Addtours,AgencyRegistration
# Create your models here.
class Customer(models.Model):
    name=models.TextField(max_length=100,null=True)
    email=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.name
    

class Applications(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    tour=models.ForeignKey(Addtours,on_delete=models.CASCADE,null=True)
    agency=models.ForeignKey(AgencyRegistration,on_delete=models.CASCADE,null=True)
    name=models.TextField(max_length=100,null=True)
    mobile=models.TextField(max_length=20,null=True)
    address=models.TextField(max_length=400,null=True)
    pincode=models.BigIntegerField(null=True)
