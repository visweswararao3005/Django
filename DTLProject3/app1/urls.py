from django.urls import path

from app1 import views

urlpatterns = [
    path('', views.home),
    path('displaydemo/', views.display),
    path('updatedemo/', views.update),
    path('adddemo/', views.add),
]