from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, ListCreateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.permissions import IsAdminUser, BasePermission
import collections
from django.core.exceptions import ObjectDoesNotExist

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated) or (request.method in SAFE_METHODS)


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
        print(apps)
        serializer = GetBriefAppSerializer(apps, many=True)
        return Response(serializer.data)


class AppDetail(APIView):
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

    def put(self, request, pk, format=None):
        myapp = App.objects.get(pk=pk)
        serializer = AppSerializer(myapp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppSubjects(ListAPIView):

    def list(self, request, *args, str):
        apps = App.objects.filter(subject=str)
        if not apps:
            return Response("there is no app by this subject or subject not found", status=status.HTTP_404_NOT_FOUND)
        serializer = GetBriefAppSerializer(apps, many=True)
        return Response(serializer.data)


class AppRate(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if float(request.data['rate']) > 5 or float(request.data['rate']) < 0:
            return Response("not valid rate.", status=status.HTTP_400_BAD_REQUEST)
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            exist = Rate.objects.filter(
                user=request.data['user'], app=request.data['app'])
            if not exist:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response("this user has rated before.", status=status.HTTP_409_CONFLICT)


class GetAppRate(ListAPIView):

    def get(self, request, *args, appid):
        rates = Rate.objects.filter(app=appid)
        sum = 0
        i = 0
        if not rates:
            return Response("this app not rated yet.", status=status.HTTP_200_OK)
            return
        for rate in rates:
            i += 1
            sum += float(rate.rate)
        result = sum/i
        return Response(result, status=status.HTTP_200_OK)


class AppComment(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = SaveCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAppComment(ListAPIView):

    def get(self, request, *args, appid):
        print(request.GET)
        comments = Comment.objects.filter(app=appid)
        if not comments:
            return Response("no comments for this app or app not found", status=status.HTTP_404_NOT_FOUND)
        serializer = GetCommentSerializer(comments, many=True)
        return Response(serializer.data)


class AppDownload(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = DownloadSerializer(data=request.data)
        if serializer.is_valid():
            exist = Download.objects.filter(
                user=request.data['user'], app=request.data['app'])
            print(exist)
            if not exist:
                serializer.save()
                myapp = App.objects.get(pk=request.data['app'])
                myapp.download_number += 1
                myapp.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response("this user has downloaded this app before.", status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        dict = {}
        list = []
        list1 = []
        number = 0
        counter = 0
        apps = App.objects.all()
        for app in apps:
            dict[app.id] = app.download_number
        sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])
        sorted_dict = collections.OrderedDict(sorted_dict)
        if len(sorted_dict) > 5:
            number = 5
        else:
            number = len(sorted_dict)
        for x in sorted_dict.keys():
            list.append(x)
        print(list)
        for x in range(number):
            list1.append(App.objects.filter(id=list.pop())[0])
        serializer = GetBriefAppSerializer(list1, many=True)
        return Response(serializer.data)


class UserBookmark(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = BookmarkSerializer(data=request.data)
        if serializer.is_valid():
            exist = Bookmark.objects.filter(
                user=request.data['user'], app=request.data['app'])
            print(exist)
            if not exist:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response("this user has bookmarked before.", status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserBookmark(ListAPIView):

    def get(self, request, *args, userid):
        bookmarks = Bookmark.objects.filter(user=userid)
        if not bookmarks:
            return Response("no bookmarks for this user or user not found", status=status.HTTP_404_NOT_FOUND)
        list = []
        for bookmark in bookmarks:
            list.append(App.objects.filter(id=bookmark.app.id)[0])
        serializer = GetBriefAppSerializer(list, many=True)
        return Response(serializer.data)


class DeleteOrGetUserBookmark(DestroyAPIView, ListAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, userid, appid):
        bookmark = Bookmark.objects.filter(
            user=userid, app=appid)
        if not bookmark:
            return Response("this user has not bookmark this app", status=status.HTTP_404_NOT_FOUND)
        Bookmark.delete(bookmark[0])
        return Response("bookmarked app deleted", status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, userid, appid):
        bookmark = Bookmark.objects.filter(user=userid, app=appid)
        if not bookmark:
            return Response("False", status=status.HTTP_404_NOT_FOUND)
        serializer = GetCommentSerializer(bookmark)
        return Response("True", status=status.HTTP_200_OK)