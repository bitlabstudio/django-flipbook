"""Models for the flipbook app."""
from django.conf import settings
from django.urls import reverse
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
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )

    slug = models.SlugField(
        max_length=100,
        verbose_name=_('Slug'),
        unique=True,
    )

    small_image = FilerImageField(
        verbose_name=_('Small image'),
        blank=True, null=True,
        related_name='flipbook_categories_with_small_images',
        on_delete=models.CASCADE,
    )

    large_image = FilerImageField(
        verbose_name=_('Large image'),
        blank=True, null=True,
        related_name='flipbook_categories_with_large_images',
        on_delete=models.CASCADE,
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

    def __str__(self):
        return self.title

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
    :image: Optional flipbook image.
    :book_type: Optional book type (e.g. to distinguish formats).
    :url: Optional external url.
    :email: Optional email address.

    """
    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('User'),
        related_name='flipbooks',
        blank=True, null=True,
        on_delete=models.CASCADE,
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
        on_delete=models.CASCADE,
    )

    slug = models.SlugField(
        max_length=100,
        verbose_name=_('Slug'),
        unique=True,
    )

    is_published = models.BooleanField(
        verbose_name=_('Is published'),
        default=False,
    )

    download = FilerFileField(
        verbose_name=_('Download'),
        blank=True, null=True,
        related_name='download_flipbooks',
        on_delete=models.CASCADE,
    )

    video_download = FilerFileField(
        verbose_name=_('Video Download'),
        blank=True, null=True,
        related_name='video_download_flipbooks',
        on_delete=models.CASCADE,
    )

    image = FilerImageField(
        verbose_name=_('Image'),
        blank=True, null=True,
        related_name='flipbooks',
        on_delete=models.CASCADE,
    )

    book_type = models.CharField(
        max_length=256,
        verbose_name=_('Type'),
        choices=getattr(settings, 'FLIPBOOK_BOOK_TYPE', (
            ('default', _('default')), )
        ),
        blank=True,
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

    def __str__(self):
        return self.title

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
    :video_url: Optional video url.
    :page_type: Optional page type (e.g. to distinguish pages in the html
      template).

    """
    flipbook = models.ForeignKey(
        Flipbook,
        verbose_name=_('Flipbook'),
        related_name='pages',
        on_delete=models.CASCADE,
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
        on_delete=models.CASCADE,
    )

    video_url = models.URLField(
        verbose_name=_('Video URL'),
        blank=True,
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

    def __str__(self):
        return str(self.position)


class FlipbookDownload(models.Model):
    """
    Model, which holds information about a flipbook download file.

    :flipbook: Flipbook, which contains this download.
    :position: Position of the download.
    :file_type: File type.
    :file: File.

    """
    flipbook = models.ForeignKey(
        Flipbook,
        verbose_name=_('Flipbook'),
        related_name='downloads',
        on_delete=models.CASCADE,
    )

    position = models.PositiveIntegerField(
        verbose_name=_('Position'),
    )

    file = FilerFileField(
        verbose_name=_('File'),
        blank=True, null=True,
        related_name='flipbook_downloads',
        on_delete=models.CASCADE,
    )

    file_type = models.CharField(
        max_length=12,
        verbose_name=_('File type'),
        choices=(
            ('pdf', _('PDF')),
            ('video', _('Video')),
        ),
        blank=True,
    )

    class Meta:
        ordering = ['position', 'flipbook', 'pk']

    def __str__(self):
        return str(self.position)
