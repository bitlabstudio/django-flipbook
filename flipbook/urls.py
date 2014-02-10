"""URLs for the ``flipbook`` app."""
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[\w-]+)/$',
        views.FlipbookDetailView.as_view(),
        name='flipbook_detail'),
    url(r'^$',
        views.FlipbookListView.as_view(),
        name='flipbook_list'),
)
