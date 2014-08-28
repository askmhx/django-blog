from django.views.generic import TemplateView
from mxblog.models import LinkGroup

__author__ = 'MengHX'


class StartView(TemplateView):

    template_name = "start.html"

    def get_context_data(self, **kwargs):
        context = super(StartView, self).get_context_data(**kwargs)
        context['linkGroups'] = LinkGroup.objects.order_by('sort')
        return context