import requests

# URL base de la API
base_url = "http://api-calculadora.softwareseguro.com.ar/verificar-codigo-calculadora/?t="

# Lista de cdigos a probar
codigos = ["A", "B", "C", "D", "ABCD"]

# Probar cada cdigo
for codigo in codigos:
    url = base_url + codigo
    print(f"[+] Probando cdigo: {codigo}")
    response = requests.get(url)

    if response.status_code == 200:
        respuesta = response.text
        print("    Respuesta:", respuesta)

        # Ver si contiene un hash
        if "HASH" in respuesta.upper():
            print("\nHASH ENCONTRADO! ")
            print("", respuesta)
            break  # Paramos el script porque ya encontramos lo que queramos
    else:
        print(f"Error al contactar la API. Cdigo: {response.status_code}")