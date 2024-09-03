from django.urls import path

from marriage import views

urlpatterns = [
    path('', views.home),
    path('display', views.display),
]