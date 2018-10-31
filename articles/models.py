from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Adoptante(models.Model):
    rut_adop = models.CharField(max_length=10,primary_key=True)
    nomb_adoptante = models.CharField(max_length = 20)
    apaterno_adoptante = models.CharField(max_length=15)
    correo_adoptante = models.EmailField()
    edad_adoptante = models.IntegerField()
    tel_adoptante = models.CharField(max_length= 12)


def __str__(self):
    return self.title
