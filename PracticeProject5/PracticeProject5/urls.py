"""
URL configuration for PracticeProject5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django.contrib
from django.urls import path, include

from PracticeProject5 import views

urlpatterns = [
    path('admin/', django.contrib.admin.site.urls),

    path('', views.home),
    path('result', views.display_result),
    path('year/', include("year.urls")),
    path('marriage/', include("marriage.urls")),
]
