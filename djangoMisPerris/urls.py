from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^$', views.inicio, name = 'inicio'),
    url(r'^Formulario/$', views.Formulario, name = 'formulario'),
    url(r'^QuienSo/', views.QuienSo, name = 'quienso'),
    url(r'^Servicio/', views.Servicio, name = 'servicio'),
    url(r'^Contacto/', views.Contacto, name = 'contacto'),
]

# urlpatterns += staticfiles_urlpatterns()
