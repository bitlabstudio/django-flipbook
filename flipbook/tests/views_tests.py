"""Tests for the views of the ``flipbook`` app."""
from django.core.urlresolvers import reverse
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin

from .factories import FlipbookFactory
from .. import views


class FlipbookDetailViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Test case for the FlipbookDetailView view."""
    view_class = views.FlipbookDetailView

    def setUp(self):
        self.flipbook = FlipbookFactory()

    def get_view_name(self):
        return 'flipbook_detail'

    def get_view_kwargs(self):
        return {'slug': self.flipbook.slug}

    def test_view(self):
        self.is_callable()
        self.flipbook.is_published = False
        self.flipbook.save()
        self.redirects(reverse('flipbook_list'))


class FlipbookListViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Test case for the FlipbookListView view."""
    view_class = views.FlipbookListView

    def setUp(self):
        self.flipbook = FlipbookFactory()

    def get_view_name(self):
        return 'flipbook_list'

    def test_view(self):
        self.is_callable()
