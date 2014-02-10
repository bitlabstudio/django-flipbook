"""Tests for the models of the ``flipbook`` app."""
from django.test import TestCase

from .factories import FlipbookFactory


class FlipbookTestCase(TestCase):
    """Tests for the ``Flipbook`` model."""
    longMessage = True

    def setUp(self):
        self.flipbook = FlipbookFactory()

    def test_model(self):
        self.assertTrue(self.flipbook.pk, msg=(
            'Should be able to instantiate and save the object.'))

    def test_get_folder_images(self):
        self.assertEqual(self.flipbook.get_folder_images().count(), 0, msg=(
            'Should return an empty image list.'))
