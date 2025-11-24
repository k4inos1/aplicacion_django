from django.core.management.base import BaseCommand
from entregables.models import Vehiculo, Operario, Faena
import random

class Command(BaseCommand):
    help = 'Aleatorizar el estado (activo/inactivo) de los datos en la base de datos'

    def handle(self, *args, **kwargs):
        self.stdout.write('Iniciando aleatorización de estados...')

        # 1. Aleatorizar Vehículos
        vehiculos = Vehiculo.objects.all()
        for v in vehiculos:
            v.estado = random.choice(['operativo', 'en_mantencion', 'fuera_servicio', 'reparacion'])
            v.save()
        self.stdout.write(f'Actualizados {vehiculos.count()} vehículos.')

        # 2. Aleatorizar Operarios
        operarios = Operario.objects.all()
        for o in operarios:
            o.activo = random.choice([True, False])
            o.save()
        self.stdout.write(f'Actualizados {operarios.count()} operarios.')

        # 3. Aleatorizar Faenas
        faenas = Faena.objects.all()
        for f in faenas:
            f.estado = random.choice(['planificada', 'en_curso', 'pausada', 'completada', 'cancelada'])
            f.save()
        self.stdout.write(f'Actualizadas {faenas.count()} faenas.')

        self.stdout.write(self.style.SUCCESS('¡Estados aleatorizados exitosamente!'))
