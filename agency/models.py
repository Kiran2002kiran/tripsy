from django.db import models

# Create your models here.
class AgencyRegistration(models.Model):
    agencyname=models.TextField(max_length=100,null=True)
    branches=models.TextField(max_length=100,null=True)
    ownername=models.TextField(max_length=100,null=True)
    userid=models.TextField(max_length=100,null=True)
    license=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)

    class Meta:
        db_table='agency'

    def __str__(self):
        return self.agencyname

class Addtours(models.Model):
    Agency=models.ForeignKey(AgencyRegistration,on_delete=models.CASCADE)
    Destination=models.TextField(max_length=100,null=True)
    Description=models.TextField(max_length=100,null=True)
    Image=models.ImageField(upload_to='addtours',null=True)
    Charge=models.FloatField(null=True)

    def __str__(self):
        return self.Agency.agencyname


  