from django.urls import path

from year import views

urlpatterns = [
    path('', views.home),
    path('display', views.display),
]