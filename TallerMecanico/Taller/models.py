from django.db import models

class Resenna(models.Model):
    texto = models.TextField()
    calificacion = models.IntegerField()

class Mecanico(models.Model):
    rut=models.CharField(primary_key=True, max_length=8)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    
    def __str__(self):
        return (self.nombre)+" "+(self.apellido)