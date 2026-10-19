# Laboratorio 2: Web Scraping, Procesamiento y Recuperación de Información

- **URL del Repositorio:** https://github.com/franciscoAlfaroF/Laboratorio2

---

## 1. Instrucciones para reproducir la ejecución (Entorno Virtual)

### 1.1. Creación y activación del entorno virtual
Desde la terminal en la raíz del proyecto, ejecute:

```powershell
# Crear el entorno virtual
py -m venv .venv

# Activar el entorno en Windows (PowerShell)
.venv\Scripts\Activate.ps1

# (Alternativa en Windows CMD)
# .venv\Scripts\activate.bat

1. requests es una librería cliente HTTP cuya función es enviar peticiones web a un servidor y recibir la respuesta. En cambio, BeautifulSoup es un analizador sintáctico (parser) que toma ese texto HTML o XML y lo transforma en un árbol de objetos de Python navegable, permitiendo buscar, filtrar y extraer elementos específicos mediante etiquetas, atributos o selectores CSS.
2. Existe el riesgo de fragilidad o rotura del scraper: si los desarrolladores del sitio web modifican la estructura del DOM, renombran clases CSS (por ejemplo, cambiar article.product_pod o p.price_color) o alteran la jerarquía de etiquetas, los selectores dejarán de encontrar los elementos, provocando que la extracción devuelva datos vacíos, incompletos o lance excepciones en tiempo de ejecución.
3. Porque permite estandarizar la representación del texto para que el vectorizador TF-IDF no trate palabras idénticas con distinta capitalización como tokens diferentes en el vocabulario.
4. fit_transform() realiza dos operaciones sobre la colección de títulos: primero aprende el vocabulario completo del corpus y calcula los pesos IDF de cada término (fit), y luego convierte cada título en su representación vectorial TF-IDF (transform), generando la matriz del índice.
5. Se muestra primero el libro con similitud 0.75, ya que los resultados se ordenan de forma descendente mediante puntuaciones.argsort()[::-1]. Una puntuación igual o cercana a cero indica que los vectores de la consulta y del título son prácticamente ortogonales, lo que significa que no comparten términos relevantes dentro del vocabulario aprendido (baja o nula coincidencia léxica).
6. Limitación: TF-IDF se basa en coincidencia léxica exacta de tokens y no comprende el significado semántico ni el contexto, además de que los títulos suelen ser textos muy cortos con poca información descriptiva sobre la temática de la obra. Mejora concreta: Incorporar la descripción/sinopsis y la categoría del libro para enriquecer el documento indexado, aplicar lematización o stemming junto con eliminación de stopwords, o bien utilizar embeddings semánticos densos para capturar similitud conceptual y sinónimos. 
