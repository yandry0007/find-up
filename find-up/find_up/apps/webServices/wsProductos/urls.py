from django.conf.urls import patterns, url

urlpatterns = patterns('find_up.apps.webServices.wsProductos.views',
    url(r'^api/findup/ws/productos/$' , 'wsProductos_view', name='ws_productos_url'), #especificar el nombre del metodo de la vista creada
    url(r'^api/findup/ws/usuarios/$' , 'wsUsuarios_view', name='ws_usuarios_url'), #especificar el nombre del metodo de la vista creada
    )
