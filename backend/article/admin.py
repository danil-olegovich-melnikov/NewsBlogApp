from django.contrib import admin
from django.utils.html import mark_safe

from . import models


# Register your models here.
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    @admin.display
    def cover_image(self, obj):
        return mark_safe(f'<img width="150" src="{obj.cover.url}" />')

    cover_image.short_description = 'Обложка'
    cover_image.allow_tags = True

    list_display = ['cover_image', 'title', 'section']
    list_filter = ['section']
    search_fields = ['title']
    readonly_fields = ['cover_image']

