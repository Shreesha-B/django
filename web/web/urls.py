from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('distance/', include('distance.urls')),
    path('admin/', admin.site.urls),
]