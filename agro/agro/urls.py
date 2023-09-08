"""
URL configuration for agro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp.views import activate
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

    path("myapp/", include("django.contrib.auth.urls")),
    
    path("accounts/profile/", views.viewprofile),
    path('', views.homepage, name= "home"),
    path('myapp/register/', views.registeruser, name='sign_up'),
    path('myapp/', include('myapp.urls')),
    path('register/', views.registeruser, name='register'),
    path('accounts/register/', views.registeruser, name='register'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
]
