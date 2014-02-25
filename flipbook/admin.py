"""Admin registration for the ``flipbook`` app."""
from django.contrib import admin
from django.db.models import TextField

from django_summernote.widgets import SummernoteWidget

import models


class FlipbookCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title', )}


class FlipbookPageInline(admin.StackedInline):
    model = models.FlipbookPage
    extra = 1
    formfield_overrides = {TextField: {'widget': SummernoteWidget}}


class FlipbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    prepopulated_fields = {'slug': ('title', )}
    inlines = [
        FlipbookPageInline,
    ]


admin.site.register(models.FlipbookCategory, FlipbookCategoryAdmin)
admin.site.register(models.Flipbook, FlipbookAdmin)
