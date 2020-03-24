from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
from .views import CodeAutoComplete, ProfAutoComplete

app_name = 'review'

urlpatterns = [
    url('^add_review/$', views.add_review, name="create"),
    url('^code-autocomplete/$', CodeAutoComplete.as_view(), name='code-autocomplete'),
    url('^prof-autocomplete/$', ProfAutoComplete.as_view(), name='prof-autocomplete'),
]
