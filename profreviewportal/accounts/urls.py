from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
from review.models import Course, Review, Prof


app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^profile/$', views.profile_view, name="profile")
]
