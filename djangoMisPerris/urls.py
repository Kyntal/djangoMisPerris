from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^$', views.inicio),
    url(r'^Formulario/$', views.Formulario),
    url(r'^QuienSo/', views.QuienSo),
    url(r'^Servicio/', views.Servicio),
    url(r'^Contacto/', views.Contacto), 
]

# urlpatterns += staticfiles_urlpatterns()
