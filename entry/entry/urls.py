"""entry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "Entry & Exit System Admin Panel"
admin.site.site_title = "Entry & Exit System"
admin.site.index_title = "Welcome to Entry & Exit System"

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('director/', include('director.urls')),
    path('gaurd/', include('gaurd.urls'))
]
