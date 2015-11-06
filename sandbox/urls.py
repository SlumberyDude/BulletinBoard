"""sandbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from sample import regbackend
from registration.backends.default.views import RegistrationView
from sample.forms import UserRegForm

urlpatterns = [
	url(r'^$', 'sample.views.home', name='home'),
	url(r'^accounts/profile/', 'sample.views.get_profile', name='profile'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=UserRegForm), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact/', 'sample.views.contact', name="contact"),
    url(r'^add_bulletin/', 'sample.views.add_bulletin', name="bulletin"),
    url(r'^get_bulletin/', 'sample.views.get_bulletin'),
]
