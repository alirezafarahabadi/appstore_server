
from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status
from .serializers import *
from django.contrib.auth import get_user_model
from django.core import serializers


# Create your views here.


class SignUp(generics.CreateAPIView):

    def post(self, request):
        serializer = SaveCustomUserSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            get_user_model().custom_user_create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPI(ListAPIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, *args, **kwargs):
        users = get_user_model().objects.all()
        serializer = CustomuserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        username = request.user.username
        user = get_user_model().objects.filter(username=username)
        print(user)
        # users = get_user_model()
        serializer = CustomuserSerializer(user, many=True)
        return Response(serializer.data)
