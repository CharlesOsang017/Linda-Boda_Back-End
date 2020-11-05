from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, PassengerSerializer
from .models import  Passenger
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django_countries.fields import CountryField
from knox.views import LoginView as KnoxLoginView

# Create your views here.

def page(request):
    
    
    

    return render(request, 'page.html')


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class PassengerList(APIView):
    def get(self, request, format=None):
        all_passenger = Passenger.objects.all()
        serializers = PassengerSerializer(all_passenger, many=True)
        return Response(serializers.data)
        
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)