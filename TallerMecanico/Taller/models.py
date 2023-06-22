from django.db import models


class Contacto(models.Model):
    idContacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=255)
    mensaje = models.TextField()

    def __str__(self):
        return str(self.nombre)

class Resenna(models.Model):
    texto = models.TextField()
    calificacion = models.IntegerField()


class Mecanico(models.Model):
    rut = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return (self.nombre)+" "+(self.apellido)

