from django.db import models

# Create your models here.


class usuario(models.Model):
    nombre = models.CharField(max_length=60, verbose_name='nombre')
    apellido = models.CharField(max_length=60, verbose_name='apellido')
    nombreUsuario = models.CharField(
        max_length=60, verbose_name='usuario')
    email = models.CharField(max_length=60, verbose_name='email')
    password = models.CharField(max_length=60, verbose_name='contraseña')

    def __str__(self):
        return self.nombre


class series(models.Model):
    titulo = models.CharField(max_length=60, verbose_name='titulo')
    origen = models.CharField(max_length=60, verbose_name='origen')
    chapters = models.CharField(
        max_length=60, verbose_name='capitulos')
    estreno = models.CharField(max_length=60, verbose_name='estreno')

    def __str__(self):
        return self.titulo
