from django.urls import path
from myapp.views import *
from myapp import views as myapp_view

urlpatterns = [
    path('', myapp_view.app_list.as_view()),
    path('<int:pk>/', myapp_view.app_detail.as_view()),
    path('comment/', myapp_view.commentAPI.as_view()),
    path('comment/<int:app_pk>/', myapp_view.commentAPI.as_view()),

]