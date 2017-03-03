from django.db import models
from django.contrib.auth.models import User

class Direccion(models.Model):
	ciudad = models.CharField(max_length=200)
	barrio = models.CharField(max_length=200)
	calle_pricipal = models.CharField(max_length=200)
	calle_secundaria = models.CharField(max_length=200)
	latitud = models.DecimalField(max_digits=6, decimal_places=2)
	longitud = models.DecimalField(max_digits=6, decimal_places=2)
	referencia = models.CharField(max_length=200)
	
	def __unicode__(self):
		return '%s - %s' %(self.ciudad, self.barrio)
	
	class Meta:
		verbose_name = 'Direccion'
		verbose_name_plural = 'Direcciones'
	
def url2(self, filename):
	ruta = "static/img/Empresas/%s/%s/"%(self.nombre, str(filename))
	return ruta
	
class Empresa(models.Model):
	def Icono(self):
		return '<a href="/%s"><img src="/%s" width=50px height=50px/></a>'%(self.imagen, self.imagen)
	
	Icono.allow_tags = True
	
	nombre = models.CharField(max_length=200)
	horario = models.CharField(max_length=200)
	imagen = models.ImageField(upload_to=url2, null=True, blank=True)
	fk_direccion = models.ForeignKey(Direccion, blank=True, null=True)
	
	def __unicode__(self):
		return self.nombre
	


def url(self, filename):
	ruta = "static/img/Productos/%s/%s/"%(self.nombre, str(filename))
	return ruta

class Categoria(models.Model):
	nombre = models.CharField(max_length=40)
	descripcion = models.TextField(max_length=200)
	
	def __unicode__(self):
		return self.nombre

class Producto(models.Model):
	
	def thumbnail(self):
		return '<a href="/%s"><img src="/%s" width=50px height=50px/></a>'%(self.imagen, self.imagen)
	
	thumbnail.allow_tags = True
	
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=200)
	precio = models.DecimalField(max_digits=6, decimal_places=2)
	stock = models.IntegerField(blank=False, default="0")
	imagen = models.ImageField(upload_to=url, null=True, blank=True)
	categorias = models.ManyToManyField(Categoria)
	fk_empresa = models.ForeignKey(Empresa)
	fk_propietario = models.ForeignKey(User)
	
	
	def __unicode__(self):
		return self.nombre
		
def url3(self, filename):
	ruta = "static/img/Perfiles/%s/%s/"%(self.user, str(filename))
	return ruta


class Perfiles(models.Model):
	
	def Foto(self):
		return '<a href="/%s"><img src="/%s" width=50px height=50px/></a>'%(self.foto, self.foto)
	
	Foto.allow_tags = True
	
	user = models.OneToOneField(User)
	nombres = models.CharField(blank=False, max_length=30)
	apellidos = models.CharField(blank=False, max_length=30)
	cedula = models.CharField(blank=True, max_length=10, unique=True, null=True)
	foto = models.ImageField(upload_to=url3, blank=True, null=True)
	correo = models.EmailField(blank=False, unique=True)
	telefono = models.IntegerField(blank=True, null=True)
	movil = models.CharField(blank=True, max_length=10, null=True)
	hombre = models.BooleanField(blank=False, default=False)
	mujer = models.BooleanField(blank=False, default=False)
	tipo_registro = models.CharField(blank=True, null=True, max_length=30, default='facebook')
	
	#tipo_login = models.CharField(blank=True, null=True, max_length=30, default='google')
	#app_nombre = models.CharField(blank=True, null=True, max_length=30, default='ktaxi')
	 
	def __unicode__(self):
		return self.user.username
	
	class Meta:
		verbose_name = 'Perfil'
		verbose_name_plural = 'Perfiles'
