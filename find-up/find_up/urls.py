
from django.conf.urls import url, include, patterns
from django.contrib import admin

urlpatterns = patterns('find_up.apps.main.views',
    url(r'^admin/', admin.site.urls),
    url(r'^',include('find_up.apps.webServices.wsProductos.urls')),
    url(r'^api/findup/producto/(?P<id_prod>.*)/$','singleProduct_view'),
    #url(r'^api/findup/login/(?P<name>.*)/(?P<password>.*)/(?P<tipo_login>.*)/$','login_view'),
    url(r'^api/findup/login/$','login_view'),
    url(r'^api/findup/logout/(?P<id_user>.*)/$','logout_view'),
    url(r'^api/findup/registrarse/(?P<usuario>.*)/(?P<nombres>.*)/(?P<apellidos>.*)/(?P<password>.*)/(?P<correo>.*)/(?P<celular>.*)/(?P<cedula>.*)/(?P<tipo_registro>.*)/$','registrarse_view'),
    url(r'^api/findup/subirimagen/(?P<imagen>.*)/$','subir_imagen_perfil_view'),
    #URL BUSQUEDA SIMPLE
    url(r'^api/findup/search/(?P<data>.*)/$','search_view'),
    )