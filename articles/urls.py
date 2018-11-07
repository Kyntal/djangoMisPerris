from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^nuevo$', views.article_list, name='article_list'),
]
