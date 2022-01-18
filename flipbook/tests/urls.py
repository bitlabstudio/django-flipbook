"""URLs to run the tests."""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^flipbooks/', include('flipbook.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
]
