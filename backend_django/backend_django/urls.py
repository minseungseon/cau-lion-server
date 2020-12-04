from django.contrib import admin
from django.urls import path, include
#from rest_framework_swagger.views import get_swagger_view

#schema_view = get_swagger_view(title = "My API")

urlpatterns = [
    #path('', get_swagger_view(title = "My API")),
    path('admin/', admin.site.urls),
    path('login-api/', include('login_api.urls')),
    path('login-api/auth', include("knox.urls")),
]
