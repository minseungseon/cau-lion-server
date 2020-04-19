from django.urls import path, include
from .views import TestAPI, RegistrationAPI, LoginAPI, UserAPI


urlpatterns = [
    path('test/', TestAPI),
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
]
