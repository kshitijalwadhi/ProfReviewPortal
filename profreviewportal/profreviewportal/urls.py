from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^review/', include('review.urls')),
    url(r'^profs/', include('profs.urls')),
    url(r'^$', views.homepage)
]
