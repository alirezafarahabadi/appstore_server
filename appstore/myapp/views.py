from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView
from .serializers import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class AppCreate(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = AppSerializer(data=request.data)
        print(request.data['apk_file'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppList(ListAPIView):
    
    def get(self, request):
        apps = App.objects.all()
        serializer = Get_brief_app_serializer(apps, many=True)
        return Response(serializer.data)


class AppDetail(RetrieveUpdateAPIView):
    """
    Retrieve, update a app instance.
    """

    def get(self, request, *args, pk):
        try:
            myapp = App.objects.get(pk=pk)
        except App.DoesNotExist:
            raise Http404
        serializer = AppSerializer(myapp)
        return Response(serializer.data)

    def put(self, request, *args, pk):
        myapp = App.objects.get(pk=pk)
        serializer = AppSerializer(App, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppSubjects(ListAPIView):

    def list(self, request, *args, str):
        queryset=App.objects.filter(subject=str)
        serializer = Get_brief_app_serializer(queryset, many=True)
        return Response(serializer.data)

