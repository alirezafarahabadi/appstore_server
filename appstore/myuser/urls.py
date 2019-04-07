from django.urls import path
from django.conf.urls import url
from . import views as userview
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', userview.signup.as_view()),
    path('login/', userview.login.as_view()),
    url(r"^api/token/$", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    url(r"^api/token/refresh/$", TokenRefreshView.as_view(), name="token_refresh"),
]