from django.shortcuts import render
from .models import custom_user
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.decorators import api_view

from django.conf import settings

from rest_framework import status
from .serializers import *
from django.contrib.auth import get_user_model

# Create your views here.


class signup(generics.CreateAPIView):

    def post(self, request, format=None):
        print("request", request.data)
        serializer = customuser_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class login(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        authentication_classes=()
        # permission_classes = (permissions.IsAuthenticated,)
        # queryset = get_user_model().objects.filter(username=request.data['username'])
        serializer = settings.AUTH_USER_MODEL
