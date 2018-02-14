from django import forms
from .models import Doctor, Patient
#......
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('profile_photo', 'name', 'hospital')

class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('doctor',)
