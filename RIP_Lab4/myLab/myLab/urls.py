"""myLab URL Configuration

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
from app.views import ListView
from app.views import NewView
from app.views import goHere




urlpatterns = [
    path('admin/', admin.site.urls),
    path('links/', NewView.as_view(), name='startPage'),
    path('links/<int:id>', ListView.as_view(), name='link_url'),
    path('links/goHere', goHere, name='goHere')
]
