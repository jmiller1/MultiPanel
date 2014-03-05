from django.conf.urls import patterns, include, url
from .views import PanelRedirectView,PanelCapturista

urlpatterns = patterns('',

	url(r'^$' , 'django.contrib.auth.views.login', {'template_name':'inicio/index.html'},
		name='login'),

	url(r'cerrar/$' , 'django.contrib.auth.views.logout_then_login', name='logout'),

	#url(r'^capturista/panel-capturista/$' , PanelCapturista.as_view() , name="panel-capturista"),

	url(r'^panel-redirect/$' , PanelRedirectView.as_view() , name="panel-redirect"),
)
