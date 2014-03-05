from django.db import models

class CapturarClientes(models.Model):
	nombre = models.CharField(max_length=100)
	domicilio = models.CharField(max_length=100)
	telefono = models.CharField(max_length=100)
	email = models.EmailField()
	rfc = models.CharField(max_length=100)
	curp = models.CharField(max_length=100)
	logo = models.ImageField(upload_to='logo_cliente')

	def __unicode__(self):
		return self.nombre

class CapturarViajes(models.Model):
	cliente = models.CharField(max_length=100)
	fecha = models.CharField(max_length=100)
	origen = models.CharField(max_length=100)
	destino = models.CharField(max_length=100)
	tracto_numero = models.CharField(max_length=100)
	caja_numero = models.CharField(max_length=100)
	hora_programada_de_salida_de_planta = models.CharField(max_length=100)
	hoara_de_salida = models.CharField(max_length=100)
	tiempo_estimado_de_llegada = models.CharField(max_length=100)
	ubicacion = models.CharField(max_length=100)
	hora = models.CharField(max_length=100)
	hora_de_llegada_patio = models.CharField(max_length=100)
	hora_de_salida_patio = models.CharField(max_length=100)
	transfer_que_lo_retira = models.CharField(max_length=100)
	observaciones = models.TextField(max_length=150)

	def __unicode__(self):
		return self.nombre