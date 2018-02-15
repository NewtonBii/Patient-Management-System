from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    title = models.CharField(max_length=20, null=True, default = 'Dr')
    description = models.CharField(max_length=20, null=True, default = 'Medical Doctor')
    name = models.CharField(max_length=200, default='Treat Me')
    phone_number = models.IntegerField(null=True, default=0)
    license_number = models.IntegerField(null=True, default =12345)
    specialty = models.CharField(max_length=200, default='Physician')
    hospital = models.CharField(max_length=200, default='Nairobi Hospital')
    profile_photo = models.ImageField(upload_to='doctor_profiles/', default='doctor_profiles/no-image.jpg')
    user = models.ForeignKey(User, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name


class NextOfKin(models.Model):
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    phone_number = models.IntegerField(default=0)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    date_given = models.DateTimeField()
    doctor_prescribed = models.ForeignKey(Doctor)
    def __str__(self):
        return self.name

class MedicalCover(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    type_of_cover = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class AllergiesAndDirectives(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField(default=0)
    gender = models.CharField(max_length=6)
    id_number = models.IntegerField(default=0)
    status = models.CharField(max_length=8)
    email = models.EmailField()
    NHIF_number = models.IntegerField(default=0)
    blood_group = models.CharField(max_length=5)
    next_of_kin = models.ForeignKey(NextOfKin, null=True)
    medications = models.ForeignKey(Medicine, null=True)
    medical_cover = models.ForeignKey(MedicalCover, null=True)
    allergies_and_directives = models.ForeignKey(AllergiesAndDirectives, null=True)
    doctor = models.ForeignKey(Doctor, null=True)
    profile_photo = models.ImageField(upload_to='patients_photo/', null=True)

class Treatment(models.Model):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    consultation_fee = models.IntegerField(default=0)
    date = models.DateTimeField()
    symptoms = models.CharField(max_length=500, null=True)
    diagnosis = models.CharField(max_length=1000)
    recommendations = models.CharField(max_length=1000, null=True)
