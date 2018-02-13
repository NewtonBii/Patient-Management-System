from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
url(r'^$', views.dashboard, name = 'dashboard'),
url(r'^accounts/profile/', views.profile, name ='myProfile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
