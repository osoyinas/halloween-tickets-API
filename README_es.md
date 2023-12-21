# Fiesta de Halloween - Gestor de Entradas

Este proyecto utiliza Django Rest Framework para gestionar la compra y códigos QR de las entradas para una fiesta de Halloween. Permite a los usuarios registrarse y recibir códigos QR por correo electrónico y verificar la autenticidad de las entradas escaneando los códigos QR.

## Requisitos Previos

Asegúrate de tener instaladas las siguientes herramientas antes de comenzar:

- Python 3.x
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

5. **Crear un Superusuario (Opcional, para administrar el sitio de administración de Django)**

    ```bash
    python manage.py createsuperuser
    ```

6. **Ejecutar el Servidor de Desarrollo**

    ```bash
    python manage.py runserver
    ```

    Visita `http://127.0.0.1:8000/` en tu navegador para acceder a la aplicación.

## Uso

1. **Acceder al Formulario de Registro**

    Abre tu navegador y visita `http://127.0.0.1:8000/registro/` para registrar a los interesados en la fiesta.

2. **Realizar Pagos y Recibir Códigos QR**

    Después de registrarse, los usuarios recibirán un correo electrónico con un código QR después de realizar el pago.

3. **Verificar Entradas**

    Usa la funcionalidad de escaneo de códigos QR para verificar si un invitado ha pagado y conocer su identidad.

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras un problema o tienes sugerencias de mejora, no dudes en abrir un problema o enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
