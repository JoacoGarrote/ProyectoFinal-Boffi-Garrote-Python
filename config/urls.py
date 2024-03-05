from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('appentrega/', include("appentrega.urls")),
    path('users/', include('users.urls')),
]
