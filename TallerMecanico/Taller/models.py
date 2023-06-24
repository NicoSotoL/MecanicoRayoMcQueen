from django.db import models

def imagen(instance, filename):
    return 'publicaciones/{0}/{1}'.format(instance.titulo, filename)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to=imagen)

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


