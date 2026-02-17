import os
import requests
from tqdm import tqdm
from constants import URL

def show_data():
    response = requests.get(f'{URL}/get-products')
    data = response.json()
    
    tqdm(range(100), ncols=50)
    print(data['products'])

def main()->None:
    while True:
        print("BIENVENIDO AL EXTRACTOR DE DATOS, ACA PUEDES BUSCAR DATOS DE UNA API NO OFICIAL DE MERCADO LIBRE")
        print("Presione 1 para ver todos los productos")
        option: int = int(input("Presione una opción: "))

        match option:
            case 1:
                show_data()
            
            case _:
                print("Opcion incorrecta")

if __name__ == "__main__":
    main()