from django.urls import path

from studentapp import views


urlpatterns = [
    path('',views.home),
    path('task/',views.task),
]