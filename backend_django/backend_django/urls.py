from django.contrib import admin
from django.urls import path, include
from homework_api import urls
from rest_framework import urls
from django.conf import settings
from django.conf.urls.static import static
#from rest_framework_swagger.views import get_swagger_view

#schema_view = get_swagger_view(title = "My API")

urlpatterns = [
    path('', include('homework_api.urls')),
    path('admin/', admin.site.urls),
    path('login_api/', include('login_api.urls')),
    path('login_api/auth', include("knox.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)