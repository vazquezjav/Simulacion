from django.urls import path

from noticias import views

urlpatterns = [
    path('api', views.ApiNoticias.as_view(), name = 'about'),
    path('texto', views.ApiNoticiasTexto.as_view(), name = 'about2')
]