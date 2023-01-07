from django.db import models
import uuid
from users.models import HealthFaculty

# Create your models here.
# Parent of the family
class Patriarch(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    nationalId=models.CharField(unique=True,null=False,blank=False,max_length=16)
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    dob=models.DateField(null=True,blank=True)
    sex = models.CharField(max_length=1, choices=SEX)
    email=models.EmailField(null=True, blank=True)
    date=models.DateField(null=True, blank=True)
    phone=models.CharField(null=True, blank=True,max_length=15)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.firstName

class Family(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    chief=models.ForeignKey(Patriarch,on_delete=models.CASCADE)
    nationalId=models.CharField(unique=True,null=True,blank=True,max_length=16)
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    dob=models.DateField(null=True,blank=True)
    sex = models.CharField(max_length=1, choices=SEX)
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(null=True, blank=True,max_length=15)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.firstName+" "+ self.nationalId

class Bill(models.Model):
    patient=models.ForeignKey(Family,on_delete=models.CASCADE)
    date=models.DateField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.patient

class Prescription(models.Model):
    bill=models.ForeignKey(Bill,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price=models.DecimalField(max_digits = 9,decimal_places=2)
    date=models.DateField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.bill

class Address(models.Model):
    Patriarch=models.OneToOneField(Patriarch, on_delete=models.CASCADE)
    province = models.CharField(max_length=100) 
    district = models.CharField(max_length=100) 
    sector = models.CharField(max_length=100) 
    village = models.CharField(max_length=100) 
    date=models.DateField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

class Processing(models.Model):

    patient=models.ForeignKey(Family,  on_delete=models.CASCADE) 
    healthFaculty=models.ForeignKey(HealthFaculty,  on_delete=models.CASCADE,null=True,blank=True) 
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.patient.firstName

class HealthClass(models.Model):
    CLASS = (
        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        ('4', 'Class 3'),
    )
    Patriarch=models.OneToOneField(Patriarch, on_delete=models.CASCADE)
    Class = models.CharField(max_length=1, choices=CLASS) 
    date=models.DateField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.Patriarch.firstName +"->"+ self.Class