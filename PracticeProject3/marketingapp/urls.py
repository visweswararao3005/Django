from django.urls import path

from marketingapp import views


urlpatterns = [
    path('',views.home),
    path('task/',views.task),
]