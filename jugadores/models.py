from django.db import models

class Jugador(models.Model):
    Nombre_del_jugador = models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.Nombre_del_jugador
