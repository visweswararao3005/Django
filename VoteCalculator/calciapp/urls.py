from django.urls import path

from calciapp import views


urlpatterns = [
    path('', views.home),
    path('read', views.display_result),
]
