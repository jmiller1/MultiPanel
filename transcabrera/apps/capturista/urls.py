from django.conf.urls import patterns, include, url
from .views import AltaCliente,ClienteRegistrado 

urlpatterns = patterns('',

	url(r'^registrocliente/$' , AltaCliente.as_view() , name="alta_cliente"),

	url(r'^clienteregistrado/$' , ClienteRegistrado.as_view() , name="cliente_registrado"),


)
