from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# 1. Registros de vehículos de transporte (camiones, camionetas, maquinaria).
class Vehiculo(models.Model):
    TIPO_CHOICES = [
        ('CAMION', 'Camión'),
        ('CAMIONETA', 'Camioneta'),
        ('MAQUINARIA', 'Maquinaria'),
        ('OTRO', 'Otro'),
    ]

    patente = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(verbose_name="Año", validators=[MinValueValidator(1900)])
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    activo = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patente} - {self.get_tipo_display()}"

# 3. Registro de operarios, turnos o cuadrillas.
class Operario(models.Model):
    TURNO_CHOICES = [
        ('MAÑANA', 'Mañana'),
        ('TARDE', 'Tarde'),
        ('NOCHE', 'Noche'),
    ]

    rut = models.CharField(max_length=12, unique=True, help_text="Formato: 12345678-9")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    turno = models.CharField(max_length=20, choices=TURNO_CHOICES)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# 2. Control de ingreso y salida de cargas.
class Carga(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_TRANSITO', 'En Tránsito'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    ]

    TIPO_MOVIMIENTO_CHOICES = [
        ('INGRESO', 'Ingreso'),
        ('SALIDA', 'Salida'),
    ]

    descripcion = models.TextField()
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    tipo_movimiento = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO_CHOICES, default='SALIDA')
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_programada = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT, related_name='cargas')
    chofer = models.ForeignKey(Operario, on_delete=models.PROTECT, related_name='cargas', help_text="Operario responsable")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} - {self.descripcion[:30]}"

# 4. Control de inventario de insumos y repuestos.
class Inventario(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    cantidad = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad})"

# 5. Gestión de mantenciones de maquinaria.
class Mantencion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='mantenciones')
    fecha = models.DateField()
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    realizado_por = models.ForeignKey(Operario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Mantención {self.vehiculo} - {self.fecha}"

# 6. Registro de visitas de seguridad o checklists operacionales.
class VisitaSeguridad(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    inspector = models.ForeignKey(User, on_delete=models.CASCADE) # Usuario del sistema (login)
    area = models.CharField(max_length=100)
    aprobado = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Visita {self.fecha.strftime('%Y-%m-%d')} - {self.area}"
