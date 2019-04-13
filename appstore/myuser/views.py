from django.http import HttpResponse
from django.http import Http404
from pytz import unicode
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
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


class UserAPI(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAdminUser,)
    def get(self, request, format=None):
        print(request.user)
        apps = get_user_model().objects.all()
        serializer = customuser_serializer(apps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = customuser_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

