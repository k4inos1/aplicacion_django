# Sistema de Gestión Forestal Industrial

Sistema web desarrollado en Django para la gestión integral de maquinaria, operarios y faenas en la industria forestal del Biobío.

## 🌲 Descripción

Esta aplicación permite a empresas forestales gestionar eficientemente sus activos y operaciones. Diseñada específicamente para el contexto industrial, incluye control de maquinaria pesada, registro de operarios con validación nacional, seguimiento de faenas y gestión de seguridad.

## 🚀 Características Principales

### Gestión de Maquinaria
- **Registro de Vehículos**: Camiones, cosechadoras, skidders, grúas.
- **Control de Mantenciones**: Alertas automáticas cada 500 horas de uso.
- **Historial**: Registro de mantenciones preventivas y correctivas.

### Gestión de Operarios
- **Registro de Personal**: Operadores, choferes, mecánicos, supervisores.
- **Validación de RUT**: Algoritmo de validación de RUT chileno integrado.
- **Perfiles**: Control de licencias y roles.

### Control de Operaciones
- **Gestión de Faenas**: Planificación y seguimiento de cortes, transporte y raleo.
- **Métricas**: Registro de metros cúbicos (m³) y hectáreas trabajadas.
- **Seguridad**: Registro y seguimiento de incidentes y accidentes.

### Seguridad y Tecnología
- **Base de Datos Industrial**: MySQL 9.5.
- **Autenticación Robusta**: Sistema de login/logout con protección de rutas.
- **Validaciones**: Control estricto de datos (fechas, rangos, formatos).
- **Auditoría**: Logging de errores y seguimiento de acciones.

## 🛠️ Requisitos Previos

- Python 3.10 o superior
- MySQL Server 8.0 o superior
- pip (gestor de paquetes de Python)

## 📦 Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/k4inos1/aplicacion_django.git
cd aplicacion_django
```

### 2. Configurar Entorno Virtual
```bash
py -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos (MySQL)

Asegúrate de tener MySQL corriendo y crea la base de datos:

```sql
CREATE DATABASE aplicacion_django CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'ADMIN'@'localhost' IDENTIFIED BY 'ForestalDB2025!';
GRANT ALL PRIVILEGES ON gestion_forestal.* TO 'ADMIN'@'localhost';
FLUSH PRIVILEGES;
```

Configura el archivo `.env` en la raíz del proyecto (o usa los defaults en settings.py):
```env
DB_ENGINE=mysql
DB_NAME=gestion_forestal
DB_USER=ADMIN
DB_PASSWORD=ForestalDB2025!
DB_HOST=localhost
DB_PORT=3306
```

### 5. Migrar Datos
```bash
py manage.py migrate
```

### 6. Crear Superusuario
```bash
py manage.py createsuperuser
```

### 7. Iniciar Servidor
```bash
py manage.py runserver
```
Accede a `http://127.0.0.1:8000/`

## 🛠️ Herramientas de Desarrollo y Gestión

El proyecto incluye comandos personalizados para facilitar el desarrollo y pruebas:

### Poblar Base de Datos (Seeding)
Genera un gran volumen de datos de prueba (vehículos, operarios, faenas, etc.) para verificar el rendimiento y la paginación.
```bash
py manage.py seed_db
```

### Aleatorizar Datos (Randomize)
Actualiza **todos** los registros existentes con valores aleatorios. Útil para probar cambios de estado, filtros y visualización de datos variados sin crear nuevos registros.
```bash
py manage.py randomize_status
```
*Nota: Este comando modifica datos existentes, incluyendo estados, fechas, costos y asignaciones.*


## 🔒 Seguridad Implementada

### Autenticación
- Todas las vistas requieren inicio de sesión (`@login_required`).
- Contraseñas almacenadas con hash seguro (PBKDF2).
- Protección contra ataques de fuerza bruta (limitación de intentos por defecto en Django).

### Validación de Datos
- **RUT Chileno**: Se valida formato y dígito verificador en el servidor.
- **Sanitización**: Los inputs son sanitizados para prevenir XSS.
- **Integridad**: Uso de transacciones y validación de claves foráneas.

### Manejo de Errores
- Bloques `try-except` en operaciones críticas.
- Sistema de logging para registrar errores sin exponer detalles al usuario.
- Mensajes de feedback (Flash Messages) para acciones del usuario.

## 🏗️ Estructura del Proyecto

```
gestion-forestal/
├── entregables/           # Aplicación principal
│   ├── models.py          # Modelos de datos (Vehiculo, Operario, Faena...)
│   ├── views.py           # Lógica de negocio y controladores
│   ├── urls.py            # Rutas de la aplicación
│   └── admin.py           # Configuración del panel administrativo
├── templates/             # Plantillas HTML
│   ├── entregables/       # Vistas del sistema
│   └── registration/      # Vistas de autenticación
├── gestion_entregables/   # Configuración del proyecto
│   ├── settings.py        # Configuración global
│   └── urls.py            # Rutas principales
└── requirements.txt       # Dependencias del proyecto
```

## 👥 Roles de Usuario

- **Administrador**: Acceso total al sistema y panel admin.
- **Supervisor**: Gestión de faenas y operarios.
- **Mecánico**: Registro de mantenciones.
- **Operador**: Visualización de tareas asignadas.

## 📄 Licencia

Este proyecto es de uso educativo para INACAP Sede Concepción-Talcahuano.
