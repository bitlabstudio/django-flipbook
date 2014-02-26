Django Flipbook
===============

A reusable Django app that displays an image gallery as a flipbook.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install django-flipbook

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://github.com/bitmazk/django-flipbook.git#egg=flipbook

TODO: Describe further installation steps (edit / remove the examples below):

Add ``flipbook`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'flipbook',
    )

Add the ``flipbook`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^flipbook/', include('flipbook.urls')),
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate flipbook


Usage
-----

Basically, there is a Flipbook and its (html) pages. You can edit them inline.

Make sure to install django-summernote, which provides the great summernote
WYSIWYG editor.
Django-App: https://github.com/lqez/django-summernote
Editor: http://hackerwins.github.io/summernote/

All flipbooks are viewed in a general list view. You can also gather flipbooks
in different categories and view them in seperated lists.

You will definitely want to overwrite the templates and add your favourite
flipbook jquery plugin, so I only added simple templates and an example plugin.
Get the plugin here:
http://tympanus.net/codrops/2012/09/03/bookblock-a-content-flip-plugin/
Thx to Tympanus so far.

Please take a look at the models.py to check the models for their fields.
There are a lot of possibilities to improve your templates. If you need any
other fields or functions feel free to send a pull request =)


Settings
--------

FLIPBOOK_BOOK_TYPE
++++++++++++++++++

Default: ('default', _('default')), )

Tuple to define different book types. This can be helpful, if you want to
distinguish different book formats etc.

FLIPBOOK_PAGE_TYPE
++++++++++++++++++

Default: ('default', _('default')), )

Tuple to define different page types. This can be helpful, if you want to
distinguish pages in your template or if you want to add special css classes
etc.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-flipbook
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
