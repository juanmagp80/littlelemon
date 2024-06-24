from django.db import models

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_reserva = models.DateField()
    ranura_reserva = models.TimeField()

    class Meta:
        unique_together = ('fecha_reserva', 'ranura_reserva')
    
    def __str__(self):
        return f"{self.nombre} - {self.fecha_reserva} - {self.ranura_reserva}"
