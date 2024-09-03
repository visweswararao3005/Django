from django.urls import path

from trainerapp import views


urlpatterns = [
    path('',views.home),
    path('task/',views.task),
]