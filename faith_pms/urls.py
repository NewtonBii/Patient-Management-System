from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
url(r'^$', views.dashboard, name = 'dashboard'),
url(r'^accounts/profile/', views.profile, name ='myProfile'),
url(r'^messages/', views.messages, name='myMessages'),
url(r'^new/profile/(?P<username>[-_\w.]+)$', views.update_profile, name='updateProfile'),
url(r'^patients/all', views.patients, name='allPatients'),
url(r'^new/patient/', views.new_patient, name='newPatient'),
url(r'^patient/(\d+)', views.single_patient, name = 'singlePatient'),
url(r'^treatment/(\d+)', views.treatment, name = 'newTreatment'),
url(r'^treatment/diagnosis/(\d+)', views.diagnosis, name = 'diagnosis')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
