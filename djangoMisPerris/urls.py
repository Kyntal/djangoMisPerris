<<<<<<< HEAD
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
=======
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
>>>>>>> c6095b82dfc81f997d4028bbd5e94d7997ce1502
