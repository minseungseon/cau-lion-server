from rest_framework.routers import DefaultRouter
from django.urls import path, include
from chatterboard_api import views

router = DefaultRouter()
router.register('bulletincontent', views.PostViewSet)

urlpatterns = [
    path('chatterboard/', include(router.urls)),
]