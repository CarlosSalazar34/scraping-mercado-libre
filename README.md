**Scraping Mercado Libre**

- **Descripción:** Proyecto pequeño para extraer listados de Mercado Libre (ej. "iPhone 17"). Incluye tres métodos: uso de la API pública, renderizado con Selenium y renderizado con Playwright.

- **Estado:** funcional; la opción recomendada es usar la API por ser más rápida y estable.

**Instalación**

- **Requisitos:** Python 3.8+ instalado en el sistema.
- **Dependencias (API):** `pip install requests beautifulsoup4`
- **Dependencias (Selenium):** `pip install selenium beautifulsoup4`  — además necesitarás descargar el `chromedriver` compatible con tu versión de Chrome y colocarlo en el `PATH` o en la misma carpeta del script.
- **Dependencias (Playwright):** `pip install playwright beautifulsoup4` y luego ejecutar `python -m playwright install` para instalar navegadores.

**Uso**

- Ejecutar el script principal:

	**Scraping Mercado Libre (Flask + BD + JS)**

	- **Descripción:** Proyecto que ofrece un endpoint Flask para recibir datos (JSON) enviados desde un script JavaScript inyectado en la página (p. ej. desde la consola del navegador). Los datos se guardan en una base local (`my_database.db`) mediante funciones en `functions.py`.

	- **Tecnologías:** `Flask`, `SQLite` (archivo `my_database.db`), JavaScript (snippet `evil.js`). Aunque mencionas MySQL, el código incluido usa SQLite; abajo explico cómo migrar si lo deseas.

	**Estructura importante**

	- Archivo principal del servidor: [main.py](main.py)
	- Lógica de BD: [functions.py](functions.py)
	- Snippet cliente (colección + POST): [evil.js](evil.js)
	- Base de datos SQLite generada: [my_database.db](my_database.db)

	**Instalación y dependencias**

	1. Crear/activar un entorno virtual (recomendado):

	```bash
	python -m venv venv
	venv\Scripts\activate
	```

	2. Instalar dependencias mínimas:

	```bash
	pip install flask flask-cors
	```

	3. (Opcional) Si vas a usar requests/BS para scraping localmente:

	```bash
	pip install requests beautifulsoup4 selenium playwright
	```

	**Cómo funciona**

	- El servidor Flask expone el endpoint `/send-data` que acepta `POST` con `Content-Type: application/json`.
	- El JS (`evil.js`) recorre elementos DOM, crea un array de objetos y lo envía con `fetch` a `http://<IP>:5000/send-data`.
	- `functions.py` crea (o recrea) una tabla `my_table` en `my_database.db` y guarda cada elemento recibido.

	**Ejecutar el servidor (desarrollo)**

	```bash
	python main.py
	```

	Por defecto arranca en `http://0.0.0.0:5000` (accesible desde la red local). Envía el POST desde el navegador al `IP` de la máquina donde corre Flask (p. ej. `http://172.20.10.3:5000/send-data`).

	**Ejemplo de uso (desde consola del navegador)**

	- Abre devtools en la página de Mercado Libre y pega el contenido de `evil.js` (o ejecútalo como bookmarklet/script) para enviar los datos al servidor.

	**Ver los datos guardados**

	- `functions.py` ya crea la tabla `my_table` y guarda `title`, `price`, `link`, `image` en `my_database.db`.
	- Para explorar la base SQLite puedes usar `DB Browser for SQLite` o desde Python:

	```python
	import sqlite3
	conn = sqlite3.connect('my_database.db')
	for row in conn.execute('SELECT * FROM my_table LIMIT 10'):
	    print(row)
	conn.close()
	```

	**Migrar a MySQL (opcional)**

	- Si prefieres MySQL, te recomiendo usar `SQLAlchemy` o `mysql-connector-python` y reemplazar las llamadas a `sqlite3` en `functions.py` por la conexión a MySQL.
	- Pasos básicos:

	  1. Instalar con: `pip install mysql-connector-python` o `pip install sqlalchemy pymysql`.
	  2. Crear la base y credenciales en el servidor MySQL.
	  3. Modificar `functions.py` para usar la conexión MySQL y ejecutar las mismas sentencias `CREATE TABLE` / `INSERT`.

	Si quieres, hago el cambio y te devuelvo `functions_mysql.py` listo para usar.

	**Seguridad y buenas prácticas**

	- No ejecutes `evil.js` en páginas sin permiso; respeta términos de servicio.
	- En producción usa CORS con origenes limitados y autentica/valida datos entrantes.
	- No dejes `debug=True` en Flask en entornos públicos.

	**Siguientes pasos que puedo hacer**

	- Añadir export CSV/JSON desde Flask.
	- Migrar `functions.py` a MySQL y/o `SQLAlchemy`.
	- Añadir endpoint para listar/consultar los registros guardados.

	Dime cuál de los siguientes quieres que implemente ahora: export CSV, migrar a MySQL, o endpoint para listar datos.

