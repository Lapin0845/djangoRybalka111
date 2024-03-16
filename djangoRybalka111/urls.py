"""
URL configuration for djangoRybalka111 project.

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
from django.contrib import admin
from django.urls import path, include
from catalog import views


urlpatterns = [
    path('admin/', admin.site.urls),
path('',views.index, name='home'),
    path('rybalka/', views.rybalka, name='rybalka'),
    path('ohota/', views.ohota, name='ohota'),
    path('odejda', views.odejda, name='odejda'),
    path('about', views.about, name='about'),
    path('cart/<int:id>', views.buy, name='buy'),
    path('cart2/<int:id>', views.buy2, name='buy2'),
    path('cart3/<int:id>', views.buy3, name='buy3'),
    path('cart4/',views.korz, name='korz'),
    path('cart/del/<int:id>', views.delete, name='del'),
    path('user/', include('django.contrib.auth.urls')),
    path('user/registr/', views.registr, name='registr'),
    path('user/login/', views.registr, name='login'),
]
