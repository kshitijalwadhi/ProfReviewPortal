from django.contrib import admin
from .models import Block, LikesCount
from datetime import datetime, timedelta
# Register your models here.
# admin.site.register(Block)
# admin.site.register(LikesCount)
admin.site.site_header = 'Administration'


def unblock_selected(modeladmin, request, queryset):
    for obj in queryset:
        obj.blockperm = False
        obj.tempban = False
        obj.end = None
        obj.save()


unblock_selected.short_description = "Unblock all selected users"


def tempban_selected(modeladmin, request, queryset):
    for obj in queryset:
        obj.blockperm = False
        obj.tempban = True
        obj.end = datetime.now() + timedelta(days=15)
        obj.save()


tempban_selected.short_description = "Block selected users for 15 days"


def permblock_selected(modeladmin, request, queryset):
    for obj in queryset:
        obj.blockperm = True
        obj.save()


permblock_selected.short_description = "Permanently Block selected users"


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('user', 'blockperm', 'tempban', 'end')
    ordering = ('user',)
    search_fields = ('user', 'blockperm', 'tempban', 'end')
    actions = [unblock_selected, tempban_selected, permblock_selected]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(LikesCount)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'userlikes')
    ordering = ('user',)
    search_fields = ('user', 'userlikes')
