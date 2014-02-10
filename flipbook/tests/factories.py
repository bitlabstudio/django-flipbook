"""Factories for the ``flipbook`` app."""
import factory

from filer.models import Folder

from ..models import Flipbook


class FolderFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Folder

    name = 'Test Folder'


class FlipbookFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Flipbook

    title = factory.Sequence(lambda i: 'name {}'.format(i))
    slug = factory.LazyAttribute(lambda a: a.title.replace(' ', '-'))
    folder = factory.SubFactory(FolderFactory)
    is_published = True
