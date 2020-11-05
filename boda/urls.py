from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI
from django.conf.urls import url, include
from django.contrib import admin
from .import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    url(r'^$', views.page, name='page'),
    url(r'^api/register/$', RegisterAPI.as_view(), name='register'),
    url(r'^api/passenger/$', views.PassengerList.as_view()),
    url(r'^api/login/$', LoginAPI.as_view(), name='login'),
    url(r'^api/logout/$', knox_views.LogoutView.as_view(), name='logout'),
    url(r'^api/logoutall/$', knox_views.LogoutAllView.as_view(), name='logoutall'),
]