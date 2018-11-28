from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth import views
from principal.views import IndexView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import inicio
from .views import Formulario
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from .views import QuienSo
from .views import Servicio
from .views import Contacto

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here5
    url(r'social-auth/', include('social_django.urls', namespace='social')),
    url(r'^$', inicio, name = 'inicio'),
    url(r'^Formulario/$', Formulario, name = 'formulario'),
    url(r'^QuienSo/', QuienSo, name = 'quienso'),
    url(r'^Servicio/', Servicio, name = 'servicio'),
    url(r'^Contacto/', Contacto, name = 'contacto'),
]

# urlpatterns += staticfiles_urlpatterns()
