from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Equipo(models.Model):
    """Modelo para representar un equipo de trabajo"""
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Equipo")
    descripcion = models.TextField(verbose_name="Descripción", blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre


class Miembro(models.Model):
    """Modelo para representar un miembro del equipo"""
    ROLES = [
        ('lider', 'Líder'),
        ('desarrollador', 'Desarrollador'),
        ('disenador', 'Diseñador'),
        ('tester', 'Tester'),
        ('analista', 'Analista'),
    ]

    nombre = models.CharField(max_length=200, verbose_name="Nombre Completo")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    rol = models.CharField(max_length=20, choices=ROLES, verbose_name="Rol")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='miembros', verbose_name="Equipo")
    fecha_ingreso = models.DateField(default=timezone.now, verbose_name="Fecha de Ingreso")
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"
        ordering = ['equipo', 'nombre']

    def __str__(self):
        return f"{self.nombre} - {self.get_rol_display()}"


class Proyecto(models.Model):
    """Modelo para representar un proyecto"""
    ESTADOS = [
        ('planificacion', 'Planificación'),
        ('en_progreso', 'En Progreso'),
        ('revision', 'En Revisión'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]

    nombre = models.CharField(max_length=200, verbose_name="Nombre del Proyecto")
    descripcion = models.TextField(verbose_name="Descripción")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='proyectos', verbose_name="Equipo")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='planificacion', verbose_name="Estado")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin_estimada = models.DateField(verbose_name="Fecha de Fin Estimada")
    fecha_fin_real = models.DateField(null=True, blank=True, verbose_name="Fecha de Fin Real")
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Presupuesto")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"{self.nombre} - {self.get_estado_display()}"


class EstadoEntregable(models.Model):
    """Modelo para representar los estados posibles de un entregable"""
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Estado")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    color = models.CharField(max_length=7, default='#6c757d', verbose_name="Color (hex)", 
                            help_text="Color en formato hexadecimal (ej: #ff0000)")
    orden = models.IntegerField(default=0, verbose_name="Orden")

    class Meta:
        verbose_name = "Estado de Entregable"
        verbose_name_plural = "Estados de Entregables"
        ordering = ['orden']

    def __str__(self):
        return self.nombre


class Entregable(models.Model):
    """Modelo para representar un entregable del proyecto"""
    PRIORIDADES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='entregables', verbose_name="Proyecto")
    responsable = models.ForeignKey(Miembro, on_delete=models.SET_NULL, null=True, related_name='entregables_asignados', verbose_name="Responsable")
    estado = models.ForeignKey(EstadoEntregable, on_delete=models.PROTECT, verbose_name="Estado")
    prioridad = models.CharField(max_length=10, choices=PRIORIDADES, default='media', verbose_name="Prioridad")
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de Vencimiento")
    fecha_completado = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Completado")
    archivo = models.FileField(upload_to='entregables/', null=True, blank=True, verbose_name="Archivo Adjunto")
    porcentaje_completado = models.IntegerField(default=0, verbose_name="% Completado", 
                                               help_text="Porcentaje de completado (0-100)")

    class Meta:
        verbose_name = "Entregable"
        verbose_name_plural = "Entregables"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.titulo} - {self.proyecto.nombre}"

    def esta_vencido(self):
        """Verifica si el entregable está vencido"""
        if self.fecha_completado:
            return False
        return timezone.now().date() > self.fecha_vencimiento


class Comentario(models.Model):
    """Modelo para comentarios en entregables"""
    entregable = models.ForeignKey(Entregable, on_delete=models.CASCADE, related_name='comentarios', verbose_name="Entregable")
    autor = models.CharField(max_length=200, verbose_name="Autor")
    contenido = models.TextField(verbose_name="Contenido")
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Comentario de {self.autor} en {self.entregable.titulo}"

