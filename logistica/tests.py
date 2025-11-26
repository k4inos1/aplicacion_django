from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Vehiculo, Carga, Operario

class LogisticaTests(TestCase):
    def setUp(self):
        # Create a user for login
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = Client()
        self.client.login(username='testuser', password='password123')

        # Create test data
        self.vehiculo = Vehiculo.objects.create(
            patente='AB-1234',
            marca='Toyota',
            modelo='Hilux',
            anio=2023,
            tipo='CAMIONETA'
        )

        self.operario = Operario.objects.create(
            rut='12345678-9',
            nombre='Juan',
            apellido='Perez',
            cargo='Chofer',
            turno='MAÑANA'
        )

    def test_dashboard_access(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_vehiculo_list(self):
        response = self.client.get(reverse('vehiculo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'AB-1234')

    def test_vehiculo_create(self):
        data = {
            'patente': 'XY-9876',
            'marca': 'Ford',
            'modelo': 'F-150',
            'anio': 2024,
            'tipo': 'CAMIONETA',
            'activo': 'on'
        }
        response = self.client.post(reverse('vehiculo_create'), data)
        self.assertEqual(response.status_code, 302) # Redirects on success
        self.assertTrue(Vehiculo.objects.filter(patente='XY-9876').exists())

    def test_carga_create(self):
        # Need to re-fetch vehiculo and operario because IDs are needed
        v_id = self.vehiculo.id
        o_id = self.operario.id

        data = {
            'descripcion': 'Carga de prueba',
            'peso_kg': 500,
            'tipo_movimiento': 'SALIDA',
            'origen': 'Bodega',
            'destino': 'Cliente',
            'fecha_programada': '2025-01-01 10:00:00', # Simplified format usually accepted by Django forms if configured or ISO
            'estado': 'PENDIENTE',
            'vehiculo': v_id,
            'chofer': o_id
        }
        # Note: Handling datetime in forms can be tricky in tests depending on input formats.
        # Using a valid ISO format often works.
        response = self.client.post(reverse('carga_create'), data)

        # If form is invalid, it returns 200 with errors.
        if response.status_code == 200:
            print(response.context['form'].errors)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Carga.objects.filter(descripcion='Carga de prueba').exists())
