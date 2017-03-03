from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import simplejson
from django.core import serializers
from find_up.apps.main.models import Producto, Perfiles
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


def leer_url_view(request,id_user,name,password):
	mensaje = {"NO FUE METODO GET":404}
	if request.method == "GET":
		try:
			#CONSULTA CON CODIGO SQL
			#nombre_user = serializers.serialize("json", User.objects.raw('SELECT * FROM auth_user where username = "'+name+'" '), fields=('is_active','username', 'first_name', 'last_name', 'email','last_login'))
			#perfil = serializers.serialize("json", Perfiles.objects.raw('SELECT * FROM main_perfiles where cedula = "'+password+'" '), fields=('nombres', 'apellidos', 'foto','foto'))
			
			#CONSULTA SIN MEXCLA DE RELACIONES
			#nombre_user = serializers.serialize("json", Perfiles.objects.filter(user__username__exact = name), fields=('nombres', 'apellidos', 'foto'))
			#print nombre_user
			
			#CONSULTA CON MEXCLA DE RELACIONES
			perfil = Perfiles.objects.filter(user__username__exact = name)
			if len(perfil) != 0:
				lista = [{'status':"success",'foto': str(p.foto), 'id': p.user.id, 'first_name': p.user.first_name, 'nombres': p.nombres, 'email:': p.user.email, 'apellidos': p.apellidos, 'is_active': p.user.is_active,'last_login': str(p.user.last_login),} for p in perfil]
				serializado = json.dumps(lista)
				return HttpResponse(serializado,content_type='application/json')
			else:
				mensaje = {"status":"failure","message":"El usuario "+name+" no existe"}
		except:
			mensaje = {"status":"failure","message":"Error en la consulta SQL"}
	return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')