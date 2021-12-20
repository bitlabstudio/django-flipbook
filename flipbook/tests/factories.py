"""Factories for the ``flipbook`` app."""
import factory

from ..models import Flipbook, FlipbookCategory, FlipbookPage, FlipbookDownload


class FlipbookCategoryFactory(factory.DjangoModelFactory):
    FACTORY_FOR = FlipbookCategory

    title = factory.Sequence(lambda i: 'name {}'.format(i))
    slug = factory.LazyAttribute(lambda a: a.title.replace(' ', '-'))


class FlipbookFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Flipbook

    title = factory.Sequence(lambda i: 'name {}'.format(i))
    slug = factory.LazyAttribute(lambda a: a.title.replace(' ', '-'))
    is_published = True


class FlipbookPageFactory(factory.DjangoModelFactory):
    FACTORY_FOR = FlipbookPage

    flipbook = factory.SubFactory(FlipbookFactory)
    position = factory.Sequence(lambda i: i)


class FlipbookDownloadFactory(factory.DjangoModelFactory):
    FACTORY_FOR = FlipbookDownload

    flipbook = factory.SubFactory(FlipbookFactory)
    position = factory.Sequence(lambda i: i)
