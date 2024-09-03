
from django.urls import path

from palindromeapp import views


urlpatterns = [
    path('',views.home),
    path('string/<str:i>/',views.string),
    path('number/<int:i>/',views.number),
]