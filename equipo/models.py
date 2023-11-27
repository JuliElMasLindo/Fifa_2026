from django.db import models

class Equipo(models.Model):
    Nombre_del_equipo = models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.Nombre_del_equipo