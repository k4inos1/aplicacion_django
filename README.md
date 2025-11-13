# Sistema de Gestión de Entregables por Equipo

Sistema web desarrollado en Django para gestionar y rastrear entregables de proyectos por equipos de trabajo.

## Descripción

Este sistema permite a las organizaciones gestionar equipos, proyectos y sus entregables de manera eficiente. Incluye funcionalidades completas de CRUD (Create, Read, Update, Delete) para equipos, proyectos y entregables, así como un panel de administración completo y un dashboard con estadísticas en tiempo real.

## Características Principales

- **CRUD Completo**: Operaciones completas de Crear, Leer, Actualizar y Eliminar para todas las entidades
- **Gestión de Equipos**: Crear, listar, editar y eliminar equipos de trabajo
- **Gestión de Proyectos**: CRUD completo de proyectos con estados, fechas y presupuestos
- **Gestión de Entregables**: CRUD completo con seguimiento de progreso, prioridades y archivos adjuntos
- **Sistema de Comentarios**: Colaboración en entregables mediante comentarios
- **Panel de Administración**: Interfaz administrativa completa con Django Admin
- **Dashboard Interactivo**: Visualización de estadísticas y métricas importantes con animaciones
- **Búsqueda y Filtros**: Búsqueda avanzada y filtros por estado, prioridad, etc.
- **Frontend Moderno**: Interfaz profesional con gradientes, animaciones y efectos interactivos
- **Diseño Responsivo**: Interfaz adaptable a dispositivos móviles y escritorio

##  Entidades del Sistema

El sistema gestiona las siguientes entidades:

1. **Equipo**: Equipos de trabajo con miembros asignados
2. **Miembro**: Integrantes de los equipos con roles específicos
3. **Proyecto**: Proyectos asociados a equipos con seguimiento de estados
4. **Entregable**: Tareas o entregables específicos de cada proyecto
5. **EstadoEntregable**: Estados personalizables para los entregables
6. **Comentario**: Sistema de comentarios para entregables

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno

## Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/k4inos1/django-app.git
cd django-app
```

### 2. Crear y Activar Entorno Virtual

**En Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

O manualmente:
```bash
pip install django python-decouple pillow
```

### 4. Configurar Variables de Entorno

Copie el archivo `.env.example` a `.env` y configure las variables:

```bash
cp .env.example .env
```

Edite el archivo `.env` con sus configuraciones:

```env
SECRET_KEY=tu-clave-secreta-aqui-genera-una-nueva
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_NAME=db.sqlite3
TIME_ZONE=America/Mexico_City
```

**IMPORTANTE**: Para producción, genere una SECRET_KEY única usando:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Aplicar Migraciones

```bash
python manage.py migrate
```

### 6. Crear Superusuario

Cree un superusuario para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Ingrese los datos solicitados:
- Nombre de usuario: (ej: admin)
- Correo electrónico: (ej: admin@example.com)
- Contraseña: (debe ser segura)

**NOTA**: No guarde las credenciales en el repositorio.

### 7. Iniciar el Servidor de Desarrollo

```bash
python manage.py runserver
```

El servidor se iniciará en: `http://127.0.0.1:8000/`

## Acceso al Sistema

### Interfaz Principal
- **URL**: http://127.0.0.1:8000/
- Navegue por las secciones: Inicio, Equipos, Proyectos, Entregables

### Panel de Administración
- **URL**: http://127.0.0.1:8000/admin/
- Use las credenciales del superusuario creado anteriormente
- Desde aquí puede gestionar todas las entidades del sistema

## Estructura del Proyecto

```
django-app/
├── gestion_entregables/     # Configuración del proyecto Django
│   ├── settings.py          # Configuraciones del proyecto
│   ├── urls.py              # URLs principales
│   └── wsgi.py              # Configuración WSGI
├── entregables/             # Aplicación principal
│   ├── models.py            # Modelos de datos (6 entidades)
│   ├── views.py             # Vistas y lógica de negocio
│   ├── urls.py              # URLs de la aplicación
│   ├── admin.py             # Configuración del admin
│   └── management/          # Comandos personalizados
├── templates/               # Plantillas HTML
│   ├── base.html           # Plantilla base
│   └── entregables/        # Templates de la app
├── static/                  # Archivos estáticos (CSS, JS)
├── media/                   # Archivos subidos por usuarios
├── manage.py               # Utilidad de Django
├── .env.example            # Ejemplo de variables de entorno
├── .gitignore              # Archivos ignorados por Git
└── README.md               # Este archivo

```

## Funcionalidades Principales

### CRUD de Equipos
- **Listar**: Ver todos los equipos con sus estadísticas
- **Crear**: Formulario para crear nuevos equipos
- **Editar**: Actualizar información de equipos existentes
- **Eliminar**: Borrar equipos (con confirmación)

### CRUD de Proyectos
- **Listar**: Ver proyectos con filtros por estado
- **Crear**: Formulario completo con fechas y presupuesto
- **Editar**: Actualizar detalles del proyecto
- **Eliminar**: Borrar proyectos (con confirmación)

### CRUD de Entregables
- **Listar**: Vista con filtros por estado y prioridad
- **Crear**: Formulario con archivos adjuntos
- **Editar**: Actualizar progreso y detalles
- **Eliminar**: Borrar entregables (con confirmación)
- **Detalle**: Vista completa con comentarios

### Dashboard
- Estadísticas generales con animaciones
- Contadores animados de números
- Proyectos en progreso
- Entregables recientes
- Acciones rápidas
- Cards interactivas con efectos hover

### Frontend Moderno
- **Diseño Visual**: Gradientes púrpura-azul en toda la interfaz
- **Animaciones**: Efectos suaves en cards, botones y elementos interactivos
- **Interactividad**: Alertas auto-dismiss, validación de formularios en tiempo real
- **Navegación**: Barra de navegación con efectos hover y indicador de página activa
- **Tablas**: Diseño moderno con gradientes en headers y efectos hover en filas
- **Formularios**: Inputs estilizados con validación visual mejorada
- **Barras de Progreso**: Animadas con gradientes
- **Badges**: Color-coded para estados y prioridades
- **Botón Back-to-Top**: Navegación rápida al inicio de la página
- **Scrollbar Personalizado**: Diseño consistente con el tema de la aplicación

## Comandos Útiles

### Desarrollo
```bash
# Iniciar servidor de desarrollo
python manage.py runserver

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Abrir shell de Django
python manage.py shell

# Recopilar archivos estáticos (para producción)
python manage.py collectstatic
```

### Testing
```bash
# Ejecutar pruebas
python manage.py test

# Verificar configuración del proyecto
python manage.py check
```

## Tecnologías Utilizadas

- **Backend**: Django 5.2.8
- **Base de Datos**: SQLite3 (desarrollo)
- **Frontend**: Bootstrap 5.3, Bootstrap Icons, Custom CSS/JS
- **Manejo de Variables de Entorno**: python-decouple
- **Manejo de Archivos**: Pillow

## Notas Importantes

### Seguridad
- **NO subir el archivo `.env`** al repositorio
- Mantener `SECRET_KEY` segura y única
- Cambiar `DEBUG=False` en producción
- Configurar `ALLOWED_HOSTS` apropiadamente en producción

### Base de Datos
- SQLite3 es adecuado para desarrollo
- Para producción considere PostgreSQL o MySQL
- El archivo `db.sqlite3` está en `.gitignore`

### Archivos Media
- Los archivos subidos se guardan en la carpeta `media/`
- Esta carpeta está en `.gitignore`
- Configure almacenamiento en la nube para producción

## 🐛 Solución de Problemas

### Error: "No module named 'django'"
```bash
pip install django python-decouple pillow
```

### Error: "Migrations not applied"
```bash
python manage.py migrate
```

### Error: "Static files not found"
```bash
python manage.py collectstatic
```

### No se puede acceder al admin
- Verifique que creó un superusuario con `python manage.py createsuperuser`
- Verifique que la URL sea correcta: `http://127.0.0.1:8000/admin/`

## Roles de Usuario

El sistema incluye los siguientes roles para miembros:
- **Líder**: Líder del equipo
- **Desarrollador**: Desarrollador de software
- **Diseñador**: Diseñador UI/UX
- **Tester**: Especialista en pruebas
- **Analista**: Analista de sistemas

## Estados de Proyectos

- Planificación
- En Progreso
- En Revisión
- Completado
- Cancelado

## Prioridades de Entregables

- **Baja**: Prioridad baja
- **Media**: Prioridad normal
- **Alta**: Requiere atención pronta
- **Crítica**: Urgente y bloqueante

## Contribuciones

Este proyecto fue desarrollado como parte de un sistema de gestión de entregables por equipo.

## Licencia

Este proyecto es de uso educativo y de demostración.

## Soporte

Para preguntas o problemas, por favor abra un issue en el repositorio de GitHub.

