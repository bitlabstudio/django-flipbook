"""URLs for the ``flipbook`` app."""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/$',
        views.FlipbookDetailView.as_view(),
        name='flipbook_detail'),
    url(r'^(?P<slug>[\w-]+)/$',
        views.FlipbookCategoryDetailView.as_view(),
        name='flipbook_category'),
    url(r'^$',
        views.FlipbookListView.as_view(),
        name='flipbook_list'),
]
