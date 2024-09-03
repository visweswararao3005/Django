from django.urls import path

from salesapp import views


urlpatterns = [
    path('',views.home),
    path('task/',views.task),
]