from django.urls import path
from django.conf.urls import url
from . import views as userview
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token



urlpatterns = [
    path('signup/', userview.signup.as_view()),
    path('', userview.UserAPI.as_view()),
    url(r'^api/token/', obtain_jwt_token),
    url(r'^api/token-refresh/', refresh_jwt_token),
    # url(r"^api/token/$", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # url(r"^api/token/refresh/$", TokenRefreshView.as_view(), name="token_refresh"),
]