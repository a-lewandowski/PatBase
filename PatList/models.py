from django.db import models

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    year_of_birth = models.DateField()
    phone = models.CharField(max_length=11)


class Visit(models.Model):
    general = models.CharField(max_length=128)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    date_visit = models.DateField(auto_now_add=True)
    details = models.TextField(null=True)


