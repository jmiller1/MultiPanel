from django.views.generic import CreateView,TemplateView
from .models import CapturarClientes,CapturarViajes
from django.core.urlresolvers import reverse_lazy

class CapturistaView(TemplateView):
	template_name = 'capturista/panel-capturista.html'

class AltaCliente(CreateView):
	template_name = 'registroclientes/altaClientes.html'
	model = CapturarClientes
	success_url = reverse_lazy('cliente_registrado')

class AltaCliente(CreateView):
	template_name = 'registroclientes/altaClientes.html'
	model = CapturarViajes
	success_url = reverse_lazy('cliente_registrado')

class ClienteRegistrado(TemplateView):
	template_name = 'registroclientes/registroClientes.html'
