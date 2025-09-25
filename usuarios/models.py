from django.db import models

class Usuario(models.Model):
    OPCIONES = [
        ('opcion1','Opción 1'),
        ('opcion2','Opción 2'),
        ('opcion3','Opción 3'),
    ]
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True)
    opcion = models.CharField(max_length=20, choices=OPCIONES)

    def __str__(self):
        return self.nombre

