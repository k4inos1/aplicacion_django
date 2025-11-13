from django.contrib import admin
from .models import Equipo, Miembro, Proyecto, EstadoEntregable, Entregable, Comentario


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo', 'fecha_creacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    date_hierarchy = 'fecha_creacion'


@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'rol', 'equipo', 'activo']
    list_filter = ['rol', 'activo', 'equipo']
    search_fields = ['nombre', 'email']
    date_hierarchy = 'fecha_ingreso'


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'equipo', 'estado', 'fecha_inicio', 'fecha_fin_estimada']
    list_filter = ['estado', 'equipo', 'fecha_inicio']
    search_fields = ['nombre', 'descripcion']
    date_hierarchy = 'fecha_inicio'


@admin.register(EstadoEntregable)
class EstadoEntregableAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'color', 'orden']
    list_editable = ['orden']
    ordering = ['orden']


@admin.register(Entregable)
class EntregableAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'proyecto', 'responsable', 'estado', 'prioridad', 'porcentaje_completado', 'fecha_vencimiento']
    list_filter = ['estado', 'prioridad', 'proyecto', 'fecha_vencimiento']
    search_fields = ['titulo', 'descripcion']
    date_hierarchy = 'fecha_creacion'
    readonly_fields = ['fecha_creacion']


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['autor', 'entregable', 'fecha_creacion']
    list_filter = ['fecha_creacion']
    search_fields = ['autor', 'contenido']
    date_hierarchy = 'fecha_creacion'

