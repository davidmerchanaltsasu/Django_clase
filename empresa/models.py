from django.db import models
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    def __str__(self):
        return f"{self.nombre} ({self.telefono})"
class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}"
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")

class Empleado(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidad)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    antiguedad = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    def __str__(self):
        return f"{self.nombre} --- {self.antiguedad}"