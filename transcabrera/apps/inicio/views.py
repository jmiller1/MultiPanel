from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView,TemplateView


class PanelRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.groups.filter(name='gerentes').count():
            return reverse_lazy('panel-gerente')
        elif user.groups.filter(name='capturistas').count():
            return reverse_lazy('panel-capturista')
        else:
            return reverse_lazy('clientes')

class PanelCapturista(TemplateView):
	template_name = 'capturista/panel-capturista.html'




