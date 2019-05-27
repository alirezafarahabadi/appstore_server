from django.urls import path
from django.conf.urls import url
from . import views as userview
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token



urlpatterns = [
    path('signup/', userview.SignUp.as_view()),
    path('profile/', userview.UserDetail.as_view()),
    path('', userview.UserListAPI.as_view()),
    url(r'^token/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),

]