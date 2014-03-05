from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	 #ADMIN
     url(r'^admin/', include(admin.site.urls)),

     #HOME
     url(r'^', include('apps.inicio.urls')),

     #CAPTURISTAS
     url(r'^capturista/', include('apps.capturista.urls')),

     #GERENTES
     #url(r'^gerentes/', include('apps.gerentes.urls')),

)
