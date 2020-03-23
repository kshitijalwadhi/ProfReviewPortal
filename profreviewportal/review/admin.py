from django.contrib import admin
from .models import Prof, Course, Review
# Register your models here.

admin.site.register(Course)
admin.site.register(Review)
admin.site.register(Prof)
