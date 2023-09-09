from django.urls import path
from .import views 

urlpatterns=[
    path('', views.login_view, name='login'),
    path('inicio',views.INICIO),

    path('contactos',views.contacto, name='contacto'),
    path('buscarcontacto/', views.buscar_contacto),
    path('eliminarcontacto/<codigo>',views.eliminarcontacto),
    path('registrarcontacto',views.registrarcontacto),
    path('editarcontacto/<codigo>',views.editarcontacto),

]