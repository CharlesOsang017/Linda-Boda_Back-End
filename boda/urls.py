from knox import views as knox_views
from .views import LoginAPI
from django.urls import path

urlpatterns = [
    url(r'^api/login/$', LoginAPI.as_view(), name='login'),
    url(r'^api/logout/$', knox_views.LogoutView.as_view(), name='logout'),
    url(r'^api/logoutall/$', knox_views.LogoutAllView.as_view(), name='logoutall'),
]