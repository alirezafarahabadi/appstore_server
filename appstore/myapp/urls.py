from django.urls import path
from myapp import views as myapp_view

urlpatterns = [
    path('create/', myapp_view.AppCreate.as_view()),
    path('rate/', myapp_view.AppRate.as_view()),
    path('', myapp_view.AppList.as_view()),
    path('<int:pk>/', myapp_view.AppDetail.as_view()),
    path('subject/<slug:str>/', myapp_view.AppSubjects.as_view()),
]
