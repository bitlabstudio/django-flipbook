"""Views for the ``flipbook`` app."""

from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView

from .models import Flipbook, FlipbookCategory


class ListViewMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if getattr(settings, "FLIPBOOK_DISABLE_LISTS", False):
            return HttpResponseRedirect("/")
        return super(ListViewMixin, self).dispatch(request, *args, **kwargs)


class FlipbookCategoryDetailView(ListViewMixin, DetailView):
    """View to display a Flipbook category."""

    model = FlipbookCategory


class FlipbookDetailView(DetailView):
    """View to display a flipbook."""

    model = Flipbook

    def dispatch(self, request, *args, **kwargs):
        self.kwargs = kwargs
        self.object = self.get_object()
        if self.object.category:
            if self.kwargs["category_slug"] != self.object.category.slug:
                return HttpResponseRedirect(reverse("flipbook_list"))
        elif self.kwargs["category_slug"] != "detail":
            return HttpResponseRedirect(reverse("flipbook_list"))
        if not self.object.is_published:
            return HttpResponseRedirect(reverse("flipbook_list"))
        return super(FlipbookDetailView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None:
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug, "is_published": True})
        else:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        obj = queryset.first()
        if queryset.count() > 1:
            # Try to get the relevant object by category
            category_slug = self.kwargs.get("category_slug")
            if category_slug:
                obj = queryset.filter(category__slug=category_slug).first()
        if not obj:
            raise Http404(
                _("No %(verbose_name)s found matching the query") % {"verbose_name": queryset.model._meta.verbose_name}
            )
        return obj


class FlipbookListView(ListViewMixin, ListView):
    """View to display a list of published flipbooks."""

    def get_queryset(self):
        return Flipbook.objects.filter(is_published=True)
