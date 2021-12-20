"""
These settings are used by the ``manage.py`` command.

With normal tests we want to use the fastest possible way which is an
in-memory sqlite database but if you want to create South migrations you
need a persistant database.

Unfortunately there seems to be an issue with either South or syncdb so that
defining two routers ("default" and "south") does not work.

"""
from south.modelsinspector import add_introspection_rules

from .test_settings import *  # NOQA


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}

INSTALLED_APPS.append('south', )


add_introspection_rules([], ["^filer\.fields\.multistorage_file\.MultiStorageFileField"])

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}
