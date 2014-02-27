"""Models for the flipbook app."""
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField


class FlipbookCategory(models.Model):
    """
    Model, which holds information about a flipbook category.

    :user: User, who owns the flipbook category.
    :title: Category title.
    :slug: Title in slug format.
    :small_image: Optional small category image.
    :large_image: Optional large category image.
    :url: Optional external url.
    :email: Optional email address.

    """
    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('User'),
        related_name='flipbook_categories',
        blank=True, null=True,
    )

    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )

    slug = models.SlugField(
        max_length=100,
        verbose_name=_('Slug'),
    )

    small_image = FilerImageField(
        verbose_name=_('Small image'),
        blank=True, null=True,
        related_name='flipbook_categories_with_small_images',
    )

    large_image = FilerImageField(
        verbose_name=_('Large image'),
        blank=True, null=True,
        related_name='flipbook_categories_with_large_images',
    )

    url = models.URLField(
        verbose_name=_('URL'),
        max_length=200,
        blank=True,
    )

    email = models.EmailField(
        verbose_name=_('eMail'),
        max_length=200,
        blank=True,
    )

    def __unicode__(self):
        return u'{0}'.format(self.title)

    def get_absolute_url(self):
        return reverse('flipbook_category', kwargs={'slug': self.slug})


class Flipbook(models.Model):
    """
    Model, which holds information about a flipbook and it's contents.

    :user: User, who owns the flipbook.
    :title: Flipbook title.
    :slug: Title in slug format.
    :category: Optional flipbook category.
    :is_published: True if the book is published or not.
    :download: Flipbook file to downlod.
    :book_type: Optional book type (e.g. to distinguish formats).

    """
    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('User'),
        related_name='flipbooks',
        blank=True, null=True,
    )

    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )

    category = models.ForeignKey(
        FlipbookCategory,
        verbose_name=_('Category'),
        blank=True, null=True,
        related_name='flipbooks',
    )

    slug = models.SlugField(
        max_length=100,
        verbose_name=_('Slug'),
    )

    is_published = models.BooleanField(
        verbose_name=_('Is published'),
        default=False,
    )

    download = FilerFileField(
        verbose_name=_('Download'),
        blank=True, null=True,
    )

    book_type = models.CharField(
        max_length=256,
        verbose_name=_('Type'),
        choices=getattr(settings, 'FLIPBOOK_BOOK_TYPE', (
            ('default', _('default')), )
        ),
        blank=True,
    )

    def __unicode__(self):
        return u'{0}'.format(self.title)

    def get_absolute_url(self):
        if self.category:
            category_slug = self.category.slug
        else:
            category_slug = 'detail'
        return reverse('flipbook_detail', kwargs={
            'slug': self.slug, 'category_slug': category_slug})


class FlipbookPage(models.Model):
    """
    Model, which holds information about a flipbook page.

    :flipbook: Flipbook, which contains this page.
    :position: Position of the page.
    :content: Page content.
    :image: Optional page image.
    :page_type: Optional page type (e.g. to distinguish pages in the html
      template).

    """
    flipbook = models.ForeignKey(
        Flipbook,
        verbose_name=_('Flipbook'),
        related_name='pages',
    )

    position = models.PositiveIntegerField(
        verbose_name=_('Position'),
    )

    content = models.TextField(
        max_length=8192,
        verbose_name=_('Content'),
        blank=True,
    )

    image = FilerImageField(
        verbose_name=_('Image'),
        blank=True, null=True,
        related_name='pages',
    )

    page_type = models.CharField(
        max_length=256,
        verbose_name=_('Type'),
        choices=getattr(settings, 'FLIPBOOK_PAGE_TYPE', (
            ('default', _('default')), )
        ),
        blank=True,
    )

    class Meta:
        ordering = ['position', 'flipbook', 'pk']

    def __unicode__(self):
        return u'{0}'.format(self.position)
