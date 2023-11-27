from django.db import models

class Tecnico(models.Model):
    Nombre_del_tecnico = models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.Nombre_del_tecnico