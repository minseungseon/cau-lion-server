from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_api/', include('login_api.urls')),
    path('login_api/auth', include("knox.urls")),
]
