from django.contrib import admin
from .models import Block, LikesCount
# Register your models here.
# admin.site.register(Block)
# admin.site.register(LikesCount)


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('user', 'block')
    ordering = ('user',)
    search_fields = ('user', 'block')


@admin.register(LikesCount)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'userlikes')
    ordering = ('user',)
    search_fields = ('user', 'userlikes')
