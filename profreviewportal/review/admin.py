from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.html import escape
from django.contrib.admin.models import DELETION
from django.contrib.admin.models import LogEntry
from django.contrib import admin
from .models import Prof, Course, Review, Warning
# Register your models here.

admin.site.site_header = 'Administration'

admin.site.register(Course)
# admin.site.register(Review)
admin.site.register(Prof)
# admin.site.register(Warning)


def remove_reported(modeladmin, request, queryset):
    for obj in queryset:
        if obj.report == True:
            obj.delete()
            tempuser = obj.author
            w = Warning(
                user=tempuser, message='Your review was deleted because it was reported by users.')
            w.save()


remove_reported.short_description = "Remove reported reviews and send warning"


def remove_reports(modeladmin, request, queryset):
    for obj in queryset:
        obj.report = False


remove_reports.short_description = "Remove reports on the selected reviews"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('code', 'prof', 'date', 'report')
    ordering = ('-date',)
    search_fields = ('code', 'prof', 'report')
    actions = [remove_reports, remove_reported]


@admin.register(Warning)
class WarningAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'date')
    ordering = ('-date',)
    search_fields = ('user', 'message')


# Reference for the below : https://medium.com/datadriveninvestor/monitoring-user-actions-with-logentry-in-django-admin-8c9fbaa3f442


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'

    # to filter the resultes by users, content types and action flags
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]


def object_link(self, obj):
    if obj.action_flag == DELETION:
        link = escape(obj.object_repr)
    else:
        ct = obj.content_type
        link = '<a href="%s">%s</a>' % (
            reverse('admin:%s_%s_change' %
                    (ct.app_label, ct.model), args=[obj.object_id]),
            escape(obj.object_repr),
        )
    return mark_safe(link)
