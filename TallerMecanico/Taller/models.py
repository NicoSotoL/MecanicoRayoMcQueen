from django.db import models

class Resenna(models.Model):
    texto = models.TextField()
    calificacion = models.IntegerField()