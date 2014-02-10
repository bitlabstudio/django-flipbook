"""Views for the ``flipbook`` app."""
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView

from .models import Flipbook


class FlipbookDetailView(DetailView):
    """View to display a flipbook."""
    model = Flipbook

    def dispatch(self, request, *args, **kwargs):
        self.kwargs = kwargs
        self.object = self.get_object()
        if not self.object.is_published:
            return HttpResponseRedirect(reverse('flipbook_list'))
        return super(FlipbookDetailView, self).dispatch(
            request, *args, **kwargs)


class FlipbookListView(ListView):
    """View to display a list of published flipbooks."""
    def get_queryset(self):
        return Flipbook.objects.filter(is_published=True)
