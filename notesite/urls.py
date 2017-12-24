"""notesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from notesite.views import home_view,login,logout,invalid_login,auth_view,register


urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^$', home_view, name='home'),
    url(r'^login/$',login,name='login'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^invalid_login/$',invalid_login,name='invalid_login'),
    url(r'^reg/$',register,name='register'),
    url(r'^notes/', include('notes.urls')),
]