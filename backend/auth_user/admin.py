from django.contrib import admin
from . import models
from django.utils.html import mark_safe


# Register your models here.
@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    @admin.display
    def image(self, obj):
        return mark_safe(f'<img width="150" src="{obj.picture.url}" />')

    image.short_description = 'Обложка'
    image.allow_tags = True

    list_display = ['image', 'user']
    search_fields = ['user']
    readonly_fields = ['image']


@admin.register(models.UserEmailVerification)
class UserEmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'code']
    search_fields = ['user']
