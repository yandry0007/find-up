from django.shortcuts import render
from django.http import HttpResponse
from find_up.apps.main.models import *
from django.contrib.auth.models import User

#Integramos la serializacion de objetos
from django.core import serializers

def wsProductos_view(request):
	#consultar a la db y validar si user existe
	data = serializers.serialize("json", Producto.objects.all())
	#retorna la info en formato json
	return HttpResponse(data,content_type='application/json')

def wsUsuarios_view(request):
	data = serializers.serialize("json", User.objects.raw('SELECT * FROM auth_user'))
	return HttpResponse(data,content_type='application/json')
