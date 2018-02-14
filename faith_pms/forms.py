from django import forms
from .models import Doctor, Patient, NextOfKin, Medicine, MedicalCover, AllergiesAndDirectives
#......
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('profile_photo', 'name', 'hospital')

class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('doctor',)

class NewNextOfKinForm(forms.ModelForm):
    class Meta:
        model = NextOfKin
        fields = ('name', 'relationship', 'phone_number', 'email')

class NewMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ('name','date_given', 'doctor_prescribed')

class MedicalCoverForm(forms.ModelForm):
    class Meta:
        model = MedicalCover
        fields = ('name', 'email', 'type_of_cover')

class AllergiesAndDirectivesForm(forms.ModelForm):
    class Meta:
        model = AllergiesAndDirectives
        fields = ('name', 'level')
