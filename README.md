# Trabajo Práctico Integrador
**Optimización de Infraestructura mediante la Virtualización de un Servidor de Servicios Integrados**

## 👥 1. Integrantes
**Materia:** Arquitectura y Sistemas Operativos
**Institución:** Universidad Tecnológica Nacional (UTN)
**Facultad:** Tecnicatura Universitaria en Programación
**Docente Tutor:** Sanchez, Santos
**Alumnos:**
  * Manchini, María Virginia
  * Martinez, Braian

---

## Objetivo del Proyecto
El objetivo principal de este proyecto es diseñar e implementar un escenario de consolidación de servicios empresariales 
(Web, Base de Datos y Archivos) dentro de un único entorno virtualizado seguro y eficiente. 

---

## Tecnologías Utilizadas
**Hipervisor:** Oracle VM VirtualBox (Tipo 2 - Hospedado)
**Sistema Operativo Invitado:** Ubuntu Server 24.04 LTS
**Lenguaje de Programación:** Python 3.12.3
**Control de Versiones:** Git y GitHub Platform

---

## Configuración de la VM (Máquina Virtual)
Para garantizar el rendimiento del servidor virtualizado, se asignaron las siguientes especificaciones:
**Nombre de la VM:** `UbuntuServer-TPI`
**Hostname del Servidor:** `srv-virtualizacion`
**Usuario Administrador:** `braian`
**Memoria RAM:** 4096 MB (4 GB)
**Procesadores:** 2 CPU vCores
**Disco Duro Virtual:** 25 GB (Almacenamiento dinámico)
**Firmware:** BIOS (EFI deshabilitado)
**Configuración de Red:** Adaptador 1 en Modo NAT (Asignación automática de IP: `10.0.2.15` vía DHCP)

---

## Estructura del Repositorio
El proyecto se encuentra organizado bajo la siguiente jerarquía de directorios para facilitar su auditoría y mantenimiento:
* `├── script_python/` Aloja el código fuente de scripts automatizados de diagnóstico.
* `├── capturas/` Almacena las evidencias gráficas del proceso de instalación.
* `├── diagramas/` Contiene esquemas lógicos de la arquitectura de la red o recursos.
* `└── documentacion/` Carpeta destinada a los informes teóricos y metodológicos en formato PDF.

---

## Descripción de `diagnostico.py`
El archivo `diagnostico.py` es un script desarrollado en Python ejecutable directamente desde la consola CLI de Ubuntu Server. 
Su propósito es actuar como una herramienta automatizada de auditoría del sistema, encargada de:
1. Detectar y validar las variables de entorno operativas.
2. Leer y mostrar en consola el Hostname configurado (`srv-virtualizacion`).
3. Diagnosticar la conectividad de la interfaz de red y comprobar el estado de los recursos de hardware lógicos asignados.

---

## Evidencias del Proyecto
El proceso técnico de laboratorio fue documentado sistemáticamente mediante capturas de pantalla :
- Configuración del hardware y definición de almacenamiento en VirtualBox.
- Proceso guiado de instalación, alta del usuario `braian` e inicio nativo del núcleo Unix.
- Comprobación remota de la red por DHCP, verificación de Python 3 y ejecución exitosa en consola del script de diagnóstico.
---

## Conclusiones
La consolidación de servicios distribuidos en una única instancia virtual con Ubuntu Server demuestra un excelente balance técnico, reduciendo costos de mantenimiento físico y maximizando el rendimiento del procesador.
La integración de un laboratorio de sistemas operativos con metodologías modernas de desarrollo simula de forma exacta los estándares reales de la industria del software.
El desarrollo integral de este TP capacita a los estudiantes en el despliegue eficiente de entornos de pruebas y producción.
