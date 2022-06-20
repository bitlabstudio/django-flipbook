"""URLs to run the tests."""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import re_path

admin.autodiscover()

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

urlpatterns += [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^flipbooks/', include('flipbook.urls')),
    re_path(r'^summernote/', include('django_summernote.urls')),
]
