"""Tests for the models of the ``flipbook`` app."""
from django.test import TestCase

from . import factories


class FlipbookCategoryTestCase(TestCase):
    """Tests for the ``FlipbookCategory`` model."""
    longMessage = True

    def setUp(self):
        self.category = factories.FlipbookCategoryFactory()

    def test_model(self):
        self.assertTrue(self.category.pk, msg=(
            'Should be able to instantiate and save the object.'))


class FlipbookTestCase(TestCase):
    """Tests for the ``Flipbook`` model."""
    longMessage = True

    def setUp(self):
        self.flipbook = factories.FlipbookFactory()

    def test_model(self):
        self.assertTrue(self.flipbook.pk, msg=(
            'Should be able to instantiate and save the object.'))


class FlipbookPageTestCase(TestCase):
    """Tests for the ``FlipbookPage`` model."""
    longMessage = True

    def setUp(self):
        self.page = factories.FlipbookPageFactory()

    def test_model(self):
        self.assertTrue(self.page.pk, msg=(
            'Should be able to instantiate and save the object.'))
