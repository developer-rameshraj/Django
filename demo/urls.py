"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from login.views import *


urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^about/$', about),
    url(r'^profile/$', profile),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^menu/$', menu),
    url(r'^admin/', admin.site.urls),
    (r'^product/$', 'products.views.index'),
    (r'^delete/(\d+)/$','products.views.delete'),
    (r'^update/(\d+)/$','products.views.update'),
)
