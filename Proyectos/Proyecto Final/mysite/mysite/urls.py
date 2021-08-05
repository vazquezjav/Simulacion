from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('app/', include('noticias.urls')),
    path('admin/', admin.site.urls),
]
