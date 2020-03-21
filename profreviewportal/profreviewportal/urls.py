from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^profs/', include('profs.urls')),
    url(r'^$',)
]
