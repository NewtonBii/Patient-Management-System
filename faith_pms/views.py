from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor
from .forms import UpdateProfileForm, NewPatientForm, NewNextOfKinForm, NewMedicineForm, MedicalCoverForm, AllergiesAndDirectivesForm
# Create your views here.
@login_required(login_url='/accounts/login')
def dashboard(request):
    current_user = request.user
    doctor = Doctor.objects.get(user_id=current_user.id)
    return render(request, 'dashboard.html', {'doctor':doctor})

def profile(request):
    current_user = request.user
    doctor = Doctor.objects.get(user_id=current_user.id)
    return render(request, 'profile.html', {'doctor':doctor})

def update_profile(request, username):
    current_user = request.user
    username = current_user.username
    doctor = Doctor.objects.get(user_id=current_user.id)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = form.save()
            doctor.user = request.user
            doctor.save()
        return redirect('myProfile')
    else:
        form = UpdateProfileForm()
    return render(request, 'update_profile.html', {'form':form, 'doctor':doctor})

def messages(request):
    current_user = request.user
    doctor = Doctor.objects.get(user_id=current_user.id)

    return render(request, 'messages.html', {'doctor':doctor, 'patients':patients})

def patients(request):
    current_user = request.user
    doctor = Doctor.objects.get(user_id=current_user.id)
    patients  = Patient.objects.all().filter(doctor=doctor)
    return render(request, 'patients.html', {'patients':patients, 'doctor':doctor})

def new_patient(request, username):
    current_user = request.user
    username = current_user.username
    doctor = Doctor.objects.get(user_id=current_user.id)
    if request.method == 'POST':
        nform = NewNextOfKinForm(request.POST, request.FILES)
        form = NewPatientForm(request.POST, request.FILES)
        if form.is_valid() and nform.is_valid():
            patient = form.save()
            patient.user = request.user
            patient.save()
        return redirect('dashboard')
    else:
        form = NewPatientForm()
        nform = NewNextOfKinForm()
        mform = NewMedicineForm()
        mcform = MedicalCoverForm()
        adform = AllergiesAndDirectivesForm()
    return render(request, 'new_patient.html', {'doctor':doctor, 'form':form, 'nform':nform, 'mform':mform, 'mcform':mcform, 'adform':adform})
