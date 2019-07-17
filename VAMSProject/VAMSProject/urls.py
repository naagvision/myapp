"""VAMSProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from newapp import views
import json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.home_view),
    url(r'^$', views.home_view),
    url(r'^search/$',views.search),
    path('cardholder/', views.cardholder_view),
    path('livemonitoring/',views.show),
    path('create/', views.create),
    path('report/', views.Employee_info_view),
    path('show/',views.show),
    path('emp',views.emp),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    path('json_data/', views.emp_view_json),
]
