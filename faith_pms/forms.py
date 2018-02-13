from django import forms
from .models import Doctor
#......
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('profile_photo', 'name', 'hospital')
