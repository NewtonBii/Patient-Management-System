from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    phone_number = models.IntegerField(default=0700000000)
    gender = models.CharField(max_length=6)
    id_number = models.IntegerField(default=00000000)
    status = models.CharField(max_length=8)
    email = models.EmailField()
    location = models.
