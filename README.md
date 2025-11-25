# Sistema de Gestión Forestal Industrial

Sistema web desarrollado en Django para la gestión integral de maquinaria, operarios y faenas en la industria forestal del Biobío.

# Sistema Forestal — Aplicación de Gestión (Django)

Aplicación web Django para la gestión de vehículos, operarios y faenas (enfoque forestal).

## Resumen
- Framework: Django
- Lenguaje: Python 3.10+ (recomendado 3.11)
- Base de datos: SQLite por defecto (desarrollo). Soporta MySQL/Postgres en producción.

## Características principales
- Gestión de Vehículos, Operarios, Faenas, Mantenciones e Incidentes
- Etiquetas visuales (badges) para `estado` con colores y fallback CSS/JS para garantizar visibilidad
- Comandos de mantenimiento: `seed_db`, `randomize_status`, `reset_db`
- Plantillas Bootstrap y JS/CSS personalizados (`static/js/main.js`, `entregables/static/css/style.css`)

## Requisitos
- Python 3.10+ (recomendado 3.11)
- pip
- (Opcional) MySQL o PostgreSQL para producción

## Instalación rápida (Windows, PowerShell)
1. Clonar repo

```pwsh
git clone https://github.com/k4inos1/aplicacion_django.git
cd aplicacion_django
```

2. Crear y activar entorno

```pwsh
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instalar dependencias

```pwsh
pip install -r requirements.txt
```

4. Migrar y crear superusuario

```pwsh
py manage.py migrate
py manage.py createsuperuser
```

5. Ejecutar servidor de desarrollo

```pwsh
py manage.py runserver
```

Accede a `http://127.0.0.1:8000/`.

## Configurar base de datos externa (opcional)
Si usas MySQL/Postgres, configura las variables de conexión en `gestion_entregables/settings.py` o a través de variables de entorno. Ejemplo `.env`:

```
DB_ENGINE=postgresql
DB_NAME=gestion_forestal
DB_USER=usuario
DB_PASSWORD=secreto
DB_HOST=127.0.0.1
DB_PORT=5432
```

## Instalación de MySQL (MySQL Installer, GUI, Windows)
Pasos rápidos para instalar MySQL con el instalador oficial en Windows:

1. Descargar MySQL Installer desde: https://dev.mysql.com/downloads/installer/ (elige la versión "Windows (x86, 64-bit), MSI Installer").
2. Ejecutar el instalador y seleccionar **Developer Default** o **Server only**.
3. Durante el asistente:
	 - Acepta las dependencias (Connector/ODBC, Tools) sugeridas.
	 - Configura el tipo de configuración (Standalone MySQL Server).
	 - Define contraseña para el usuario `root` (guárdala de forma segura).
	 - Asegúrate de que el servicio MySQL quede configurado para iniciarse automáticamente.
4. Finaliza la instalación y prueba conexión desde PowerShell:
```pwsh
mysql -u root -p
```
Ingresa la contraseña para verificar que puedes acceder.

5. Crear la base de datos y usuario para la aplicación (ajusta `TuPasswordSeguro!`):
```sql
CREATE DATABASE gestion_forestal CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'gestion_user'@'localhost' IDENTIFIED BY 'TuPasswordSeguro!';
GRANT ALL PRIVILEGES ON gestion_forestal.* TO 'gestion_user'@'localhost';
FLUSH PRIVILEGES;
```

Notas:
- Si el driver Python que uses muestra errores de autenticación (plugin `caching_sha2_password`), ejecuta:
	```sql
	ALTER USER 'gestion_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'TuPasswordSeguro!';
	FLUSH PRIVILEGES;
	```
- Para desarrollo Windows recomiendo `PyMySQL` (fácil de instalar). Para producción `mysqlclient` ofrece mejor rendimiento.


## Comandos útiles
- `py manage.py seed_db` — Poblado masivo de datos para pruebas (vehículos, operarios, faenas, etc.).
- `py manage.py randomize_status` — Aleatoriza estados y algunos campos para probar vistas.
- `py manage.py reset_db [--seed]` — Revierte y reaplica migraciones; con `--seed` vuelve a poblar.

**Atención**: `randomize_status` y `reset_db --seed` pueden modificar registros; usar solo en entornos de prueba.

## Frontend: badges y visibilidad (nota técnica)
Durante desarrollo detectamos que algunas manipulaciones del DOM ocultaban las etiquetas de estado temporalmente. Para robustecer la visualización se aplicaron tres medidas:

1. Las celdas de estado (`td`) incluyen `data-estado` y `data-estado-label` en las plantillas.
2. `static/js/main.js` contiene funciones defensivas (`ensureStatusBadges`) y `MutationObserver` que restauran badges si se eliminan o se les cambia el estilo.
3. Fallback CSS: `td[data-estado]::after { content: attr(data-estado-label); }` — esto asegura que el texto del estado aparezca incluso si un script borra nodos hijos.

Si notas problemas visuales, realiza un hard-refresh (Ctrl+F5) y revisa la consola del navegador para mensajes del observer.

## Estructura del proyecto (resumen)
```
aplicacion_django/
├── entregables/                # App principal (models, views, templates, management)
│   ├── management/commands/    # seed_db, reset_db, randomize_status
│   ├── migrations/
│   └── templates/entregables/
├── gestion_entregables/        # settings.py, urls.py
├── static/                     # assets globales
├── db.sqlite3                   # BD de desarrollo (opcional)
├── manage.py
└── requirements.txt
```

## Desarrollo y contribuciones
- Usa ramas descriptivas y PR.
- Añade tests para cambios de lógica.
- Mantén `requirements.txt` actualizado.

## Troubleshooting rápido
- Si las etiquetas desaparecen: hard-refresh + abrir DevTools (F12) → Console. Los observers emiten logs cuando restauran badges.
- Si el servidor no arranca: ejecuta `py manage.py check` y revisa errores en consola.

---
