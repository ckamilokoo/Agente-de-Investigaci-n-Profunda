# 🚀 FastAPI Report Generator

Este proyecto es una API construida con **FastAPI** que utiliza **Langchain** y la **API de búsqueda de Tavily** para generar informes técnicos detallados sobre un tema proporcionado por el usuario.  
El sistema planifica la estructura del informe, realiza búsquedas web relevantes para cada sección y luego ensambla un informe final en formato **Markdown**.

---

## 📁 Estructura del Proyecto

````bash
├── app/
│   ├── main.py                      # Archivo principal de FastAPI
│   ├── models/                      # Modelos Pydantic para la API
│   │   ├── __init__.py
│   │   ├── report.py
│   ├── routers/                     # Rutas de la API
│   │   ├── __init__.py
│   │   ├── report_generation.py
│   ├── core/                        # Lógica principal (Langchain, Tavily)
│   │   ├── __init__.py
│   │   ├── config.py                # Configuración y claves API
│   │   ├── search.py                # Funciones de búsqueda web
│   │   ├── prompts.py               # Prompts de Langchain
│   │   ├── report_planning.py       # Plan del reporte
│   │   ├── section_processing.py    # Procesamiento de secciones
│   │   ├── report_generation_logic.py # Orquestación del reporte con LangGraph
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── formatting.py            # Formateo de resultados y secciones
├── requirements.txt                 # Dependencias del proyecto
├── .env                             # Variables de entorno (claves API)
└── README.md                        # Este archivo



## ✅ Requisitos

* Python 3.7 o superior

## ⚙️ Instalación

1.  Clona el repositorio:

    ```bash
    git clone [https://github.com/tu_usuario/fastapi_report_generator.git](https://github.com/tu_usuario/fastapi_report_generator.git)
    cd fastapi_report_generator
    ```

2.  Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate        # En Linux/macOS
    venv\Scripts\activate           # En Windows
    ```

3.  Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## 🔐 Configuración

1.  Crea un archivo `.env` en la raíz del proyecto.
2.  Agrega tus claves API:

    ```ini
    OPENAI_API_KEY=tu_clave_de_openai
    TAVILY_API_KEY=tu_clave_de_tavily
    ```

    ⚠️ **Importante:** Reemplaza `tu_clave_de_openai` y `tu_clave_de_tavily` con tus claves reales. No subas este archivo a GitHub.

## 🚀 Uso

1.  Ejecuta la aplicación con Uvicorn:

    ```bash
    uvicorn app.main:app --reload
    ```

    Esto iniciará el servidor en: `http://127.0.0.1:8000`

2.  Envía una solicitud POST a `/generate_report/` con el siguiente cuerpo JSON:

    ```json
    {
      "topic": "El impacto de la IA en la medicina moderna"
    }
    ```

    Puedes usar herramientas como `curl`, Postman o Insomnia.

    Ejemplo con `curl`:

    ```bash
    curl -X POST -H "Content-Type: application/json" \
      -d '{"topic": "El impacto de la IA en la medicina moderna"}' \
      [http://127.0.0.1:8000/generate_report/](http://127.0.0.1:8000/generate_report/)
    ```

3.  La API devolverá un informe en formato Markdown bajo la clave `final_report`.

## 🧠 Arquitectura del Proyecto

* `app/main.py`: Punto de entrada de FastAPI.
* `app/models/`: Modelos Pydantic para la validación de datos.
* `app/routers/`: Define el endpoint `/generate_report/`.
* `app/core/`:
    * `config.py`: Carga de variables y claves API.
    * `search.py`: Lógica para usar la API de Tavily.
    * `prompts.py`: Prompts para guiar la IA.
    * `report_planning.py`: Planificación inicial del informe.
    * `section_processing.py`: Generación de búsquedas por sección.
    * `report_generation_logic.py`: Flujo completo usando LangGraph.
* `app/utils/`: Funciones auxiliares como formateo de resultados.
* `.env`: Variables de entorno sensibles.
* `requirements.txt`: Lista de dependencias.
* `README.md`: Este archivo.

## 🛠️ Tecnologías Utilizadas

* **FastAPI** – Framework web moderno y rápido.
* **Langchain** – Aplicaciones con modelos de lenguaje.
* **LangGraph** – Flujos complejos con agentes.
* **Tavily API** – Búsqueda web inteligente.
* **Pydantic** – Validación y configuración basada en tipos.
* **python-dotenv** – Carga de variables desde `.env`.
* **Uvicorn** – Servidor ASGI para FastAPI.
````
