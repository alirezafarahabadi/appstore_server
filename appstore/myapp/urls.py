from django.urls import path
from myapp import views as myapp_view

urlpatterns = [
    path('create/', myapp_view.AppCreate.as_view()),
    path('rate/<int:appid>/', myapp_view.GetAppRate.as_view()),
    path('rate/', myapp_view.AppRate.as_view()),
    path('bookmark/<int:userid>/<int:appid>/', myapp_view.DeleteUserBookmark.as_view()),
    path('bookmark/<int:userid>/', myapp_view.GetUserBookmark.as_view()),
    path('bookmark/', myapp_view.UserBookmark.as_view()),
    path('download/', myapp_view.AppDownload.as_view()),
    path('comment/<int:appid>/', myapp_view.GetAppComment.as_view()),
    path('comment/', myapp_view.AppComment.as_view()),
    path('', myapp_view.AppList.as_view()),
    path('<int:pk>/', myapp_view.AppDetail.as_view()),
    path('subject/<slug:str>/', myapp_view.AppSubjects.as_view()),
]
