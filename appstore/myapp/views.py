from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import app, download, bookmark
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.conf.urls.static import static




class app_list(APIView):
    """
    List all apps, or create a new app.
    """

    def get(self, request, format=None):
        print("hiiiiiiiiiiiiiiiiiiiiiii!")
        apps = app.objects.all()
        serializer = get_app_serializer(apps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = save_app_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class app_detail(APIView):
    """
    Retrieve, update or delete a app instance.
    """

    def get_object(self, pk):
        try:
            return app.objects.get(pk=pk)
        except app.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        apps = self.get_object(pk)
        serializer = get_app_serializer(apps)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        apps = self.get_object(pk)
        serializer = save_app_serializer(apps, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        apps = self.get_object(pk)
        apps.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class commentAPI(APIView):
    print("fg")
