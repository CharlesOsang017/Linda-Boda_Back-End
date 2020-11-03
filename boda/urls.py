from .views import RegisterAPI
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
]