"""Models for the flipbook app."""
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField
from filer.models.imagemodels import Image


class Flipbook(models.Model):
    """
    Model, which holds information about a flipbook and it's contents.

    :user: User, who owns the flipbook.
    :title: Flipbook title.
    :slug: Title in slug format.
    :folder: Linked folder of the filer app.
    :is_published: True if the book is published or not.
    :download: Flipbook file to downlod.

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

    slug = models.SlugField(
        max_length=100,
        verbose_name=_('Slug'),
    )

    folder = FilerFolderField(
        verbose_name=_('Folder'),
    )

    is_published = models.BooleanField(
        verbose_name=_('Is published'),
        default=False,
    )

    download = FilerFileField(
        verbose_name=_('Download'),
        blank=True, null=True,
    )

    def __unicode__(self):
        return u'{0}'.format(self.title)

    def get_absolute_url(self):
        return reverse('flipbook_detail', kwargs={'slug': self.slug})

    def get_folder_images(self):
        """
        Returns a set of images, which have been placed in this folder.

        """
        qs_files = self.folder.files.instance_of(Image)
        return qs_files.filter(is_public=True)
