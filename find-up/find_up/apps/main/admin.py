from django.contrib import admin
from find_up.apps.main.models import *

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'thumbnail', 'precio', 'stock', 'fk_empresa','fk_propietario')
	#list_filter = ('nombre', 'precio')
	search_fields = ['nombre', 'precio']
	fields = ('nombre', 'descripcion', ('precio', 'stock', 'imagen'),'fk_empresa','fk_propietario', 'categorias')
	#list_select_related = ('fk_empresa',)

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('nombre','horario','fk_direccion','Icono')
	search_fields = ['nombre']

class DireccionAdmin(admin.ModelAdmin):
	list_display = ('ciudad','barrio','latitud','longitud','referencia','calle_pricipal','calle_secundaria')
	search_fields = ['ciudad']

class PerfilesAdmin(admin.ModelAdmin):
	list_display = ('cedula','user','nombres','apellidos','correo','movil','tipo_registro','Foto')
	search_fields = ['cedula']

#============================================
# class MembershipInline(admin.TabularInline):
#     model = Membership
#     extra = 1

# class ProAdmin(admin.ModelAdmin):
# 	list_display = ('nombre', 'thumbnail', 'precio', 'stock', 'fk_empresa','fk_propietario')
# 	inlines = (MembershipInline,)

# class CatAdmin(admin.ModelAdmin):
#     inlines = (MembershipInline,)
#============================================



	
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Direccion, DireccionAdmin)
admin.site.register(Categoria)
admin.site.register(Perfiles,PerfilesAdmin)
