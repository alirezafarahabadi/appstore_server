from django.http import HttpResponse
from django.http import Http404
from pytz import unicode
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication


from rest_framework import status
from .serializers import *
from django.contrib.auth import get_user_model


# Create your views here.


class signup(generics.CreateAPIView):

    def post(self, request, format=None):
        print("request", request.data)
        serializer = customuser_serializer(data=request.data)
        if serializer.is_valid():
            get_user_model().create_user(**serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class login(APIView):
    def get(self, request, *args, **kwargs):
        authentication_classes = (JWTAuthentication,)
        permission_classes = (IsAuthenticated,)
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
