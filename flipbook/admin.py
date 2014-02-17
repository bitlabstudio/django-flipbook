"""Admin registration for the ``flipbook`` app."""
from django.contrib import admin

import models


class FlipbookCategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'slug')
    prepopulated_fields = {'slug': ('title', )}


class FlipbookAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'slug', 'is_published')
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(models.FlipbookCategory, FlipbookCategoryAdmin)
admin.site.register(models.Flipbook, FlipbookAdmin)
