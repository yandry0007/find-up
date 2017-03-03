from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import simplejson
from django.core import serializers
from find_up.apps.main.models import Producto, Perfiles

#ASI LAS URL JSON
#https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452
from django.contrib.auth.models import User
import json
def singleProduct_view(request,id_prod):
	if request.method == "POST":
		if "producto_id" in request.POST:
			try:
				id_pro = request.POST['producto_id']
				print "id = "+id_prod# NO LLEGA EL ATRIBUTO producto_id solo llega cambiando el orden de los demo y stock
				m = Producto.objects.get(pk=id_prod )# id_pro y id_prod se pasan a -1 ...id_prod no muestra mensajes etc..
				mensaje = {"stock":10,"producto_id":m.id}# agregar el status para mayor control
				#Modificar los datos en la BD (total y stok)
				m.stock = m.stock - 1 #fijar nuevo stock ....hacer algo mas avanzado jeje
				if m.stock >= 0:
					m.save() #guardamos la info	
				else:
					return HttpResponse(simplejson.dumps({'No':'ok'}),content_type='application/json')
			except:
				mensaje = {"stock":0}
				return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
	
	pro = Producto.objects.get(id=id_prod)
	ctx = {'pro':pro}
	return render_to_response('producto.html',ctx,context_instance=RequestContext(request))

#LOGIN CON PARAMETROS ?user=yandry&password=yandry&tipo_login=facebook&app=ktaxi
from django.contrib.auth import authenticate, login
def login_view(request):
	mensaje = {'hola':'holaa'}
	req = request.get_full_path() #OBTIENE LA URL Y PARAMETROS LIMPIOS DE DOMINIO
	arreglo_parametros = []
	parametros = {};
	try:
		if (req.find("?") > 0 ):
			url_data = req.split("?");
			arreglo_parametros = url_data[1].split("&") 
			for i in range(len(arreglo_parametros)):
				parametro = arreglo_parametros[i]
				param_data = parametro.split("=")
				parametros[param_data[0]] = param_data[1]
	except Exception, e:
		pass
	#AUTENTIFICAR USER AND PASSWORD
	print parametros['user']
	print parametros['password']
	print parametros['tipo_login']
	print parametros['app']
	# if parametros['tipo_login'] == 'facebook':
	# 	mensaje = [{"status":"success","message":"Ingresado con facebook"}]
	
	try:
		log_user = authenticate(username=parametros['user'], password=parametros['password'])
		if log_user is not None:
			#OJO CREAR UNA NUEVA TABLA PARA GUARDAR tipo_login y app
			usuario = Perfiles.objects.filter(user__username__exact = parametros['user'])
			if len(usuario) != 0:
				lista = [{'status':"success",'foto': str(p.foto), 'id': p.user.id, 'nombres': p.nombres, 'email': p.user.email, 'apellidos': p.apellidos, 'is_active': p.user.is_active,} for p in usuario]
				serializado = json.dumps(lista)
				return HttpResponse(serializado,content_type='application/json')
			else:
				mensaje = [{"status":"failure","message":"Error el la consulta SQL (filter)"}]
		else:
			mensaje = [{"status":"failure","message":"Usuario o clave incorrecta"}]
	except:
		mensaje = [{"status":"failure","message":"Error en la consulta SQL "}]
	return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')


#LOGIN CON PARAMETROS /error/con/los/slashs/
# def login_view(request,name,password,tipo_login):
# 	mensaje = {"NO FUE METODO GET":404}
# 	if request.method == "GET":
# 		try:
# 			#CONSULTA CON CODIGO SQL
# 			#nombre_user = serializers.serialize("json", User.objects.raw('SELECT * FROM auth_user where username = "'+name+'" '), fields=('is_active','username', 'first_name', 'last_name', 'email','last_login'))
# 			#perfil = serializers.serialize("json", Perfiles.objects.raw('SELECT * FROM main_perfiles where cedula = "'+password+'" '), fields=('nombres', 'apellidos', 'foto','foto'))
# 			#CONSULTAR EN AMBRAS TABLAS SQL
			
# 			#CONSULTA SIN MEXCLA DE RELACIONES
# 			#nombre_user = serializers.serialize("json", Perfiles.objects.filter(user__username__exact = name), fields=('nombres', 'apellidos', 'foto'))
# 			#print nombre_user
			
# 			#OBTENER PASSWORD DE USUARIO
# 			#clave = Perfiles.objects.filter(user__password__exact = password)
			
# 			#CONSULTA CON MEXCLA DE RELACIONES (OBTENER USUARIO Y PASSWORD)
# 			usuario = Perfiles.objects.filter(user__username__exact = name).filter(user__password__exact = password)
# 			if len(usuario) != 0:
				
# 				lista = [{'status':"success",'foto': str(p.foto), 'id': p.user.id, 'nombres': p.nombres, 'email': p.user.email, 'apellidos': p.apellidos, 'is_active': p.user.is_active,} for p in usuario]
# 				serializado = json.dumps(lista)
# 				return HttpResponse(serializado,content_type='application/json')
# 			else:
# 				mensaje = [{"status":"failure","message":"Usuario o clave incorrecta"}]
# 		except:
# 			mensaje = [{"status":"failure","message":"Error en la consulta SQL"}]
# 	return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

def logout_view(request,id_user):
	#CERRAR SESION EN EL SERVIDOR
	mensaje = {"status":"success","message":"Gracias por su tiempo"}
	return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

#url(r'^api/findup/registrarse/(?P<usuario>.*)/(?P<nombres>.*)/(?P<apellidos>.*)/(?P<password>.*)/(?P<correo>.*)/(?P<celular>.*)/(?P<cedula>.*)/(?P<tipo_registro>.*)/$','registrarse_view'),
def registrarse_view(request,usuario,nombres,apellidos,password,correo,celular,cedula,tipo_registro):
	
	try:
		u = User.objects.filter(username__exact=usuario)
		c = Perfiles.objects.filter(cedula__exact=cedula)
		if len(c) == 0:
			if len(u) == 0:
				#PARA OMITIR PARAMETROS EN URL DECLARAR COMO STRINGS
				user = User.objects.create_user(username=usuario,email=correo,password=password,first_name=nombres,last_name=apellidos)
				Perfiles.objects.create(user=user,nombres=nombres,apellidos=apellidos,correo=correo,cedula=cedula,movil=celular,tipo_registro=tipo_registro)
				#GUARDAR EL REGISTRO DEL USUARIO
				mensaje = {"status":"success","message":"Usuario, "+usuario+" registrado satisfactoriamente"}
				return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
			else:
				mensaje = {"status":"exist","message":"Usuario ya existe"} 
		else:
			mensaje = {"status":"exist","message":"Cedula ya existe"} 
	except:
		mensaje = {"status":"failure","message":"Error al registrarse"}
	return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')


def subir_imagen_perfil_view(request,imagen):
	mensaje = {"status":"success","message":"Imagen subida satisfactoriamente"}
	return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

def search_view(request, data):
	try:
		producto = Producto.objects.filter(nombre__icontains = data)
		print producto
		if len(producto) != 0:
			lista = [{'status':"success",'foto': str(p.imagen),'producto': p.nombre,'ciudad':p.fk_empresa.fk_direccion.ciudad,
			'calle principal':p.fk_empresa.fk_direccion.calle_pricipal,'calle secundaria':p.fk_empresa.fk_direccion.calle_secundaria,
			'latitud':str(p.fk_empresa.fk_direccion.latitud),'longitud':str(p.fk_empresa.fk_direccion.longitud),
			'barrio':p.fk_empresa.fk_direccion.barrio,'horario': p.fk_empresa.horario, 'empresa': p.fk_empresa.nombre,} for p in producto]
			result = json.dumps(lista)
			return HttpResponse(result,content_type='application/json')
		else:
			mensaje = [{"status":"failure","message":"Producto no encontrado"}]
	except:
		mensaje = [{"status":"failure","message":"Error sql"}]
	return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')



