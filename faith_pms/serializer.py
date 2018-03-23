# import serializers module from the rest_framework package
from rest_framework import serializers

# import UserInformation class from the models module
from .models import Doctor

# create a UserInformationSerializer class that will inhertit form the ModelSerializer class
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('title', 'description', 'name', 'phone_number', 'license_number', 'specialty', 'hospital', 'profile_photo', 'user', 'email')
