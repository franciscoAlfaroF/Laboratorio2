import requests
from bs4 import BeautifulSoup
import re

URL = "https://books.toscrape.com/"

MAPA_ESTRELLAS = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def obtener_libros() -> list[dict]:
    respuesta = requests.get(URL, timeout=10)
    respuesta.raise_for_status()
    respuesta.encoding = "utf-8"  # Asegura la correcta lectura del símbolo £
    
    soup = BeautifulSoup(respuesta.text, "html.parser")
    articulos = soup.select("article.product_pod")
    
    libros = []
    for idx, art in enumerate(articulos, start=1):
        try:
            # 1. Título (desde el atributo 'title' del enlace dentro de h3)
            tag_a = art.select_one("h3 a")
            if not tag_a or not tag_a.get("title"):
                print(f"[Advertencia] Libro #{idx} sin título válido. Se omite.")
                continue
            titulo = tag_a["title"].strip()

            # 2. Precio (limpiando el símbolo £ y convirtiendo a float)
            tag_precio = art.select_one("p.price_color")
            precio_texto = tag_precio.get_text(strip=True) if tag_precio else "0.0"
            precio_limpio = re.sub(r"[^\d.]", "", precio_texto)
            precio = float(precio_limpio) if precio_limpio else 0.0

            # 3. Disponibilidad
            tag_disp = art.select_one("p.instock.availability")
            disponibilidad = tag_disp.get_text(strip=True) if tag_disp else "Desconocida"

            # 4. Calificación en estrellas (entero de 1 a 5)
            tag_rating = art.select_one("p.star-rating")
            clases = tag_rating.get("class", []) if tag_rating else []
            calificacion = 0
            for c in clases:
                if c in MAPA_ESTRELLAS:
                    calificacion = MAPA_ESTRELLAS[c]
                    break

            libros.append({
                "titulo": titulo,
                "precio": precio,
                "disponibilidad": disponibilidad,
                "calificacion": int(calificacion)
            })

        except Exception as e:
            # Gestión de errores: se documenta en consola y continúa el ciclo
            print(f"[Error gestionado] Fallo al procesar el elemento #{idx}: {e}")
            continue

    return libros


if __name__ == "__main__":
    lista_libros = obtener_libros()
    print(f"Total de libros extraídos: {len(lista_libros)}\n")
    print("Primeros 5 registros:")
    for libro in lista_libros[:5]:
        print(libro)


