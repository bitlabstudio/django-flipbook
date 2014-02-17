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

There's a list and a detail view, so you can start right away. You can also
gather flipbooks in categories and view filtered lists. You will definitely
want to overwrite the templates and add your favourite flipbook jquery plugin,
so I only added simple templates and an example plugin. Get the plugin here:
http://tympanus.net/codrops/2012/09/03/bookblock-a-content-flip-plugin/
Thx to Tympanus so far.


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
