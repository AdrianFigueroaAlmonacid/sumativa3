from django.db import models

# Create your models here.


class usuario(models.Model):
    nombre = models.CharField(max_length=60, verbose_name='nombre')
    apellido = models.CharField(max_length=60, verbose_name='apellido')
    nombreUsuario = models.CharField(
        max_length=60, verbose_name='usuario')
    email = models.CharField(max_length=60, verbose_name='email')
    password = models.CharField(max_length=60, verbose_name='contraseña')

    def _str_(self):
        return self.nombre
