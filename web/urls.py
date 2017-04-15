from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^alta$', views.alta, name='alta'),
	url(r'^inicio$', views.index, name='index'),
	url(r'^turismo$',views.lista_turismo,name='turismo'),
	url(r'^turismo/(?P<nombreSitio>[-\w\s]+)/$',views.lugar_turismo,name='detalleTurismo'),
	url(r'^gastronomia$',views.lista_gastronomia,name='gastronomia'),
	url(r'^gastronomia/(?P<nombreLocal>[-\w\s]+)/$',views.lugar_local,name='detalleLocal'),
	url(r'^nuevo_comentario$', views.anadir_comentario, name='nuevo_comentario'),	
	url(r'^mostrar_comentarios/(?P<nombreLocal>[-\w\s]+)/$', views.mostrar_comentarios, name='mostrar_comentarios'),	
]