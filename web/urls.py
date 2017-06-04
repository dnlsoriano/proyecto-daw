from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^alta$', views.alta, name='alta'),
	url(r'^inicio$', views.index, name='index'),
	url(r'^logout$', views.peticion_logout, name='logout'),
	url(r'^turismo$',views.lista_turismo,name='turismo'),
	url(r'^turismo/(?P<nombreSitio>[-\w\s]+)/$',views.lugar_turismo,name='detalleTurismo'),
	url(r'^gastronomia$',views.lista_gastronomia,name='gastronomia'),
	url(r'^gastronomia/(?P<nombreLocal>[-\w\s]+)/$',views.lugar_local,name='detalleLocal'),
	url(r'^panel_administrador$', views.panel_administrador, name='adminsite'),	
	url(r'^panel_administrador/nuevo_local/$', views.nuevo_local, name='nuevo_local'),
	url(r'^panel_administrador/editar-local/(?P<nombreLocal>[-\w\s]+)/$', views.editar_local, name='editar_local'),
	url(r'^panel_administrador/eliminar_local/(?P<nombreLocal>[-\w\s]+)/$', views.eliminar_local, name='eliminar_local'),	
	url(r'^panel_administrador/editar-imagen-local/(?P<nombreLocal>[-\w\s]+)/$', views.editar_imagen_local, name='editar_imagen_local'),	
	url(r'^panel_administrador/lista_locales/$', views.lista_locales, name='lista_locales'),
	url(r'^panel_administrador/nuevo_turismo/$', views.nuevo_turismo, name='nuevo_turismo'),
	url(r'^panel_administrador/editar-turismo/(?P<nombreSitio>[-\w\s]+)/$', views.editar_turismo, name='editar_turismo'),
	url(r'^panel_administrador/eliminar_turismo/(?P<nombreSitio>[-\w\s]+)/$', views.eliminar_turismo, name='eliminar_turismo'),
	url(r'^panel_administrador/editar-imagen-turismo/(?P<nombreSitio>[-\w\s]+)/$', views.editar_imagen_turismo, name='editar_imagen_turismo'),	
	url(r'^panel_administrador/lista_turismo/$', views.lista_turism, name='lista_turismo'),	
	url(r'^contacto$', views.contacto, name='contacto'),	
	url(r'^nuevo_comentario$', views.anadir_comentario, name='nuevo_comentario'),	
	url(r'^mostrar_comentarios/(?P<nombreLocal>[-\w\s]+)/$', views.mostrar_comentarios, name='mostrar_comentarios'),
	url(r'^filtrar_nombre$',views.filtrar_nombre,name='filtrar_nombre'),
]