"""project URL Configuration

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
from django.urls import path

from ads.views import home, ad_detail
from users.views import login, logout, register

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ads/<int:ad_pk>', ad_detail, name='ad_detail'),

    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register'),

    path('', home, name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
