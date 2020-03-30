from django.contrib import admin
from .models import Block, LikesCount
# Register your models here.
# admin.site.register(Block)
# admin.site.register(LikesCount)
admin.site.site_header = 'Administration'


def unblock_selected(modeladmin, request, queryset):
    for obj in queryset:
        obj.block = False
        obj.save()


unblock_selected.short_description = "Unblock all selected users"


def block_selected(modeladmin, request, queryset):
    for obj in queryset:
        obj.block = True
        obj.save()


block_selected.short_description = "Block selected users"


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('user', 'block')
    ordering = ('user',)
    search_fields = ('user', 'block')
    actions = [unblock_selected, block_selected]


@admin.register(LikesCount)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'userlikes')
    ordering = ('user',)
    search_fields = ('user', 'userlikes')
