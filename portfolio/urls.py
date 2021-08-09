"""portfolio URL Configuration

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
from django.urls import path
from blog.views import index, home, about, thoughts, thought, login
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('adminpage/', admin.site.urls),
    path('index/', index, name='index'),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('thoughts/', thoughts, name='thoughts'),
    path('thoughts/thought/<slug:slug>/', thought, name='thought'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
