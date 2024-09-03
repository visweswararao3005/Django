
from django.urls import path
from armsrtongapp import views


urlpatterns = [
    path('',views.home),
    path('check/<int:i>',views.check)
]