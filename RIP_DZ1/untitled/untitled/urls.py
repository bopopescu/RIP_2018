"""untitled URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from Registaration import views as RegV
from LogIn import views as LogV
from products import views as ProdV
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',RegV.Registration.as_view(),name='Registration'),
    path('index/',RegV.Index.as_view(), name='index'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('log/', LogV.loginClass.as_view(),name='log'),
    path('profile',login_required(LogV.loginProfile.as_view(),login_url='/log/'), name='profile'),
    path('',LogV.indexRedirect, name='baseUrl'),
    # path('profile_update/<int:id>/', login_required(ProdV.AddProduct.as_view(), login_url='/log/'),
                  # name='profile_update'),#убрать
    path('profile_update/<int:id>/', ProdV.AddProduct.as_view(), name='profile_update'),
    path('profile_add',ProdV.AddNewProduct.as_view(), name='profile_add')
    # path('profile_add',login_required(ProdV.AddNewProduct.as_view(), login_url='/log/'),name='profile_add') # убрать
    # path('profile_add',group_required(['redactors'])(ProdV.AddNewProduct.as_view()),name='profile_add')# убрать
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
