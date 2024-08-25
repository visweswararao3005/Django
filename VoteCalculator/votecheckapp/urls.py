from django.urls import path

from votecheckapp import views

urlpatterns = [
    path('', views.home),
    path('display', views.check),
]