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
    url('^course/', views.review_list, name="course"),
    url(r'^search/$', views.search, name='search'),
    url('^add_prof/$', views.add_prof, name="createprof"),
    url('^add_course/$', views.add_course, name="createcourse"),
    url('report/$', views.add_report, name="post_report"),
    url('like/$', views.add_like, name="add_likes")
]
