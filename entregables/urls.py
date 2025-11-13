from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.index, name='index'),
    
    # Equipos CRUD
    path('equipos/', views.equipo_list, name='equipo_list'),
    path('equipos/crear/', views.equipo_create, name='equipo_create'),
    path('equipos/<int:pk>/editar/', views.equipo_update, name='equipo_update'),
    path('equipos/<int:pk>/eliminar/', views.equipo_delete, name='equipo_delete'),
    
    # Proyectos CRUD
    path('proyectos/', views.proyecto_list, name='proyecto_list'),
    path('proyectos/crear/', views.proyecto_create, name='proyecto_create'),
    path('proyectos/<int:pk>/editar/', views.proyecto_update, name='proyecto_update'),
    path('proyectos/<int:pk>/eliminar/', views.proyecto_delete, name='proyecto_delete'),
    
    # Entregables CRUD
    path('entregables/', views.entregable_list, name='entregable_list'),
    path('entregables/crear/', views.entregable_create, name='entregable_create'),
    path('entregables/<int:pk>/', views.entregable_detail, name='entregable_detail'),
    path('entregables/<int:pk>/editar/', views.entregable_update, name='entregable_update'),
    path('entregables/<int:pk>/eliminar/', views.entregable_delete, name='entregable_delete'),
]
