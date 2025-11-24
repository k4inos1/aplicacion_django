-- Crear base de datos
CREATE DATABASE IF NOT EXISTS gestion_forestal CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Crear usuario (si no existe)
CREATE USER IF NOT EXISTS 'forestal_user'@'localhost' IDENTIFIED BY 'ForestPass2024!';

-- Dar permisos
GRANT ALL PRIVILEGES ON gestion_forestal.* TO 'forestal_user'@'localhost';

-- Aplicar cambios
FLUSH PRIVILEGES;
