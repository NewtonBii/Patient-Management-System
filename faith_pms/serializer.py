# import serializers module from the rest_framework package
from rest_framework import serializers

# import UserInformation class from the models module
from .models import Doctor, Patient

# create a UserInformationSerializer class that will inhertit form the ModelSerializer class
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('title', 'description', 'name', 'phone_number', 'license_number', 'specialty', 'hospital', 'profile_photo', 'user', 'email')

class PatientSerializer(serializers.ModelSerializer):
    model = Patient
    fields = ('name', 'date_of_birth', 'phone_number', 'gender', 'id_number', 'status', 'email', 'NHIF_number', 'blood_group', 'next_of_kin', 'medications', 'medical_cover', 'allergies_and_directives', 'doctor', 'profile_photo')
