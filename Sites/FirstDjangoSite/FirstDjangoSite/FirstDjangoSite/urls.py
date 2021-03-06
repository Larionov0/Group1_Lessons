"""FirstDjangoSite URL Configuration

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
from django.shortcuts import HttpResponse

from django.conf import settings
from django.conf.urls.static import static


def test_view(request):
    print('О да, оно пришло!!!!')
    return HttpResponse('<h1>Привет из Джанго!:)</h1><a href="/main/first">На первую вьюху</a>')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('main/', include('MainApp.urls')),
    path('auth/', include('auth_sys.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
