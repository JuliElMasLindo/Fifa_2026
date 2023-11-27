from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('usuarios/equipo', views.equipo, name='equipo' ),
    path('usuarios/equipo/<int:equipo_id>/', views.detalle_equipo, name='detalle_equipo'),
    path('usuarios/jugadores', views.jugador, name='jugadores'),
    path('usuarios/contacto', views.contacto, name='contacto'),
    path('usuarios/tecnicos', views.tecnico, name='tecnico'),
    
    path('admin/', admin.site.urls),
]
