from selenium import webdriver
import time

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

    driver.quit()
