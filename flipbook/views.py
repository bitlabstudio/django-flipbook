"""Views for the ``flipbook`` app."""
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView

from .models import Flipbook, FlipbookCategory


class ListViewMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if getattr(settings, 'FLIPBOOK_DISABLE_LISTS', False):
            return HttpResponseRedirect('/')
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
            if self.kwargs['category_slug'] != self.object.category.slug:
                return HttpResponseRedirect(reverse('flipbook_list'))
        elif self.kwargs['category_slug'] != 'detail':
            return HttpResponseRedirect(reverse('flipbook_list'))
        if not self.object.is_published:
            return HttpResponseRedirect(reverse('flipbook_list'))
        return super(FlipbookDetailView, self).dispatch(
            request, *args, **kwargs)


class FlipbookListView(ListViewMixin, ListView):
    """View to display a list of published flipbooks."""
    def get_queryset(self):
        return Flipbook.objects.filter(is_published=True)
