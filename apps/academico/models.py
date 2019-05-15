from django.db import models

class Curso(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length=70)
	costo = models.IntegerField()
	cant_modulos = models.IntegerField()
	observaciones = models.CharField(max_length=2000, null=True)

	def __str__(self):
		return '{}'.format(self.nombre)


class Ugel(models.Model):
	id= models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	director = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.nombre)


class Inscrito(models.Model):
	id = models.IntegerField(primary_key = True)
	nombres = models.CharField(max_length=70)
	apellidos = models.CharField(max_length=70)
	dni= models.IntegerField()
	telefono = models.IntegerField()
	direccion = models.CharField(null=True,max_length=150)
	curso = models.ForeignKey(Curso,null=True, blank=True, on_delete='CASCADE')
	ugel = models.ForeignKey(Ugel, null=True, blank=True, on_delete='CASCADE')
	beneficiario = models.CharField(null=True,max_length=100, blank=True)
	modulos_entregados=models.CharField(max_length=2000, blank=True,null=True)
	asesora = models.CharField(null=True,max_length=50)
	fecha_matricula = models.DateTimeField(null=True)
	fecha_diploma = models.DateField(null=True)
	promocion = models.CharField(max_length=200, null=True)
	descuento_actual = models.IntegerField(null=True)
	descuento_pendiente = models.IntegerField(null=True)
	observaciones = models.CharField(max_length=2000, null=True, blank=True)

	def __str__(self):
		return '{} {}'.format(self.nombres, self.apellidos)
