from django.contrib import admin
from .models import Patient, Doctor, NextOfKin, Medicine, MedicalCover, AllergiesAndDirectives, Treatment

# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(NextOfKin)
admin.site.register(Medicine)
admin.site.register(MedicalCover)
admin.site.register(AllergiesAndDirectives)
admin.site.register(Treatment)
