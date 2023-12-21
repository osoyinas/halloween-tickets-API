# Fiesta de Halloween - Gestor de Entradas

Este proyecto utiliza Django Rest Framework para gestionar la compra de entradas y códigos QR para una fiesta de Halloween. Permite a los usuarios registrarse, recibir códigos QR por correo electrónico y verificar la autenticidad de las entradas escaneando códigos QR.

## Requisitos Previos

Asegúrate de tener instaladas las siguientes herramientas antes de comenzar:

- Python 3.8
- pip (administrador de paquetes de Python)

## Instalación

1. **Clonar el Repositorio**

    ```bash
    git clone https://github.com/tuusuario/fiesta-halloween.git
    cd fiesta-halloween
    ```

2. **Configurar el Entorno Virtual**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En sistemas basados en Unix
    ```

    ```powershell
    .\venv\Scripts\activate  # En Windows PowerShell
    ```

3. **Instalar Dependencias**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar la Base de Datos**

    ```bash
    python manage.py migrate
    ```

5. **Crear un Superusuario (Opcional, para el Sitio de Administración de Django)**

    ```bash
    python manage.py createsuperuser
    ```

6. **Ejecutar el Servidor de Desarrollo**

    ```bash
    python manage.py runserver
    ```

    Visita `http://127.0.0.1:8000/` en tu navegador para acceder a la aplicación.

## Uso

1. **Registro de Entradas**

    Para registrar al titular y a los acompañantes, realiza una solicitud POST al endpoint `/api/tickets/`.

2. **Generación de QR y Envío de Correo Electrónico**

    Después de que el administrador marca la entrada como pagada, los usuarios recibirán un correo electrónico con un código QR después de realizar el pago.

3. **Verificación de Entradas**

    Utiliza la funcionalidad de escaneo de códigos QR para verificar si un invitado ha pagado e identificarlos. Este QR redirigirá a `/api/tickets/<id>`.
