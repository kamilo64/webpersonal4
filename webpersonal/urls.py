"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from pages.urls import pages_patterns
from core import views as core_views
from producto import views as producto_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_views.home,name="home"),
    path('about/',core_views.about,name='about'),
    path('producto/',producto_views.producto,name='producto'),
    path('accounts/', include('registration.urls')),
    path('profiles/', include(profiles_patterns)),
    path('messenger/', include(messenger_patterns)),
    path('pages/', include(pages_patterns)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/',core_views.contact,name='contact'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static (settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)