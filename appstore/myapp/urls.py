from django.urls import path
from myapp import views as myapp_view

urlpatterns = [
    path('', myapp_view.AppList.as_view()),
    path('<int:pk>/', myapp_view.AppDetail.as_view()),
    path('subject/<slug:str>/', myapp_view.AppSubjects.as_view()),
]
