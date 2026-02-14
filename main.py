import requests
from bs4 import BeautifulSoup

def main()->None:
    URL = 'https://listado.mercadolibre.com.ve/iphone-17?sb=all_mercadolibre#D[A:iphone%2017]'
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "es-MX,es;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }
    
    try:
        page = requests.get(URL, headers=HEADERS, timeout=10)
        # page.raise_for_status()
        
        soup = BeautifulSoup(page.text, 'lxml')
        
        # Buscar items de productos (ajustado para Mercado Libre)
        # Mercado Libre utiliza diferentes selectores, probamos múltiples opciones
        items = soup.find_all('li', class_='ui-search-layout__item') or \
                soup.find_all('div', class_='ui-search-result') or \
                soup.find_all('div', {'data-component-type': 's-search-result'})
        
        print(f"Se encontraron {len(items)} productos\n")
        
        if len(items) == 0:
            # Si no se encontraron items, mostrar la estructura HTML para debug
            print("No se encontraron productos con los selectores esperados.")
            print("\nEstructura HTML (primeros 2000 caracteres):")
            print(soup.prettify()[:2000])
        else:
            for i, item in enumerate(items[:10], 1):
                try:
                    # Nombre
                    titulo = item.find('h2') or item.find('a', class_='ui-search-link')
                    nombre = titulo.text.strip() if titulo else "No disponible"
                    
                    # Precio
                    precio = item.find('span', class_='price-tag-fraction')
                    if not precio:
                        precio = item.find('div', class_='ui-search-price__main-container')
                    precio_text = precio.text.strip() if precio else "No disponible"
                    
                    # Link
                    link = item.find('a', class_='ui-search-link')
                    url_producto = link.get('href') if link else "No disponible"
                    
                    print(f"{i}. {nombre}")
                    print(f"   Precio: {precio_text}")
                    print(f"   Link: {url_producto}\n")
                    
                except Exception as e:
                    print(f"Error extrayendo producto {i}: {e}\n")
                
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")


if __name__ == "__main__":
    main()