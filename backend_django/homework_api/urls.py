from rest_framework.routers import DefaultRouter
from django.urls import path, include
from homework_api import views

router = DefaultRouter()
router.register('blogcontent', views.PostViewSet)
router.register('album', views.ImageViewSet)
router.register('files', views.FilesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]