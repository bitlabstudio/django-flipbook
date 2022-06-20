"""URLs for the ``flipbook`` app."""
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/$',
            views.FlipbookDetailView.as_view(),
            name='flipbook_detail'),
    re_path(r'^(?P<slug>[\w-]+)/$',
            views.FlipbookCategoryDetailView.as_view(),
            name='flipbook_category'),
    re_path(r'^$',
            views.FlipbookListView.as_view(),
            name='flipbook_list'),
]
