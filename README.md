# Halloween Party - Ticket Manager

This project uses Django Rest Framework to manage ticket purchase and QR codes for a Halloween party. It allows users to register, receive QR codes via email, and verify the authenticity of tickets by scanning QR codes.

## Prerequisites

Make sure you have the following tools installed before getting started:

- Python 3.x
- pip (Python package manager)

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/halloween-party.git
    cd halloween-party
    ```

2. **Set Up the Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Unix-based systems
    ```

    ```powershell
    .\venv\Scripts\activate  # On Windows PowerShell
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the Database**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser (Optional, for Django Admin Site)**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Usage

1. **Access the Registration Form**

    Open your browser and go to `http://127.0.0.1:8000/registration/` to register interested individuals for the party.

2. **Make Payments and Receive QR Codes**

    After registration, users will receive an email with a QR code after making a payment.

3. **Verify Tickets**

    Use the QR code scanning functionality to check if a guest has paid and identify them.

## Contributions

Contributions are welcome! If you find a bug or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
