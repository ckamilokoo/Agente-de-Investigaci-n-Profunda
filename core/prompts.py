
DEFAULT_REPORT_STRUCTURE = """La estructura del informe debe centrarse en desglosar el tema proporcionado por el usuario
                              y construir un informe completo en markdown utilizando el siguiente formato:


                              1. Introducción (no se necesita búsqueda web)
                                    - Breve visión general del área del tema


                              2. Secciones principales del cuerpo:
                                    - Cada sección debe centrarse en un subtema del tema proporcionado por el usuario
                                    - Incluir cualquier concepto clave y definiciones
                                    - Proporcionar ejemplos del mundo real o estudios de caso cuando sea aplicable


                              3. Conclusión (no se necesita búsqueda web)
                                    - Apuntar a 1 elemento estructural (ya sea una lista o tabla) que destile las secciones del cuerpo principal
                                    - Proporcionar un resumen conciso del informe


                              Al generar la respuesta final en markdown, si hay caracteres especiales en el texto,
                              como el símbolo de dólar, asegúrese de escaparlos correctamente para una representación correcta, por ejemplo, $25.5 debe convertirse en \$25.5
                          """
                          

REPORT_PLAN_QUERY_GENERATOR_PROMPT = """Eres un escritor experto en informes técnicos, ayudando a planificar un informe.

El informe estará centrado en el siguiente tema:
{topic}

La estructura del informe seguirá estas pautas:
{report_organization}

Tu objetivo es generar {number_of_queries} consultas de búsqueda que ayudarán a recopilar información completa para planificar las secciones del informe.

La consulta debe:
1. Estar relacionada con el tema
2. Ayudar a satisfacer los requisitos especificados en la organización del informe

Haz que la consulta sea lo suficientemente específica como para encontrar fuentes relevantes y de alta calidad, cubriendo la profundidad y amplitud necesarias para la estructura del informe.
"""


REPORT_PLAN_SECTION_GENERATOR_PROMPT = """Eres un escritor experto en informes técnicos, ayudando a planificar un informe.

Tu objetivo es generar el esquema de las secciones del informe.

El tema general del informe es:
{topic}

El informe debe seguir esta estructura organizacional:
{report_organization}

Debes reflexionar sobre esta información adicional del contexto de las búsquedas web para planificar las secciones principales del informe:
{search_context}

Ahora, genera las secciones del informe. Cada sección debe tener los siguientes campos:
- Nombre - Nombre de esta sección del informe.
- Descripción - Visión general de los temas y conceptos principales que se tratarán en esta sección.
- Investigación - Si se debe realizar una búsqueda web para esta sección del informe o no.
- Contenido - El contenido de la sección, que dejarás en blanco por ahora.

Considera qué secciones requieren búsqueda web.
Por ejemplo, la introducción y la conclusión no requerirán investigación porque destilarán información de otras partes del informe.
"""


REPORT_SECTION_QUERY_GENERATOR_PROMPT = """Tu objetivo es generar consultas de búsqueda web dirigidas que recopilen información completa para escribir una sección de informe técnico.

Tema para esta sección:
{section_topic}

Al generar {number_of_queries} consultas de búsqueda, asegúrate de que:
1. Cubran diferentes aspectos del tema (por ejemplo, características clave, aplicaciones del mundo real, arquitectura técnica)
2. Incluyan términos técnicos específicos relacionados con el tema
3. Apunten a información reciente incluyendo marcadores de año cuando sea relevante (por ejemplo, "2024")
4. Busquen comparaciones o diferenciadores de tecnologías/enfoques similares
5. Busquen tanto documentación oficial como ejemplos de implementación práctica

Tus consultas deben ser:
- Lo suficientemente específicas como para evitar resultados genéricos
- Técnicas para capturar información detallada de implementación
- Diversas para cubrir todos los aspectos del plan de la sección
- Enfocadas en fuentes autorizadas (documentación, blogs técnicos, artículos académicos)"""


SECTION_WRITER_PROMPT = """Eres un escritor técnico experto que está creando una sección específica de un informe técnico.

Título para la sección:
{section_title}

Tema para esta sección:
{section_topic}

Pautas para escribir:

1. Exactitud técnica:
- Incluir números de versión específicos
- Referenciar métricas/indicadores concretos
- Citar documentación oficial
- Utilizar la terminología técnica de manera precisa

2. Longitud y estilo:
- Límite estricto de 150-200 palabras
- No usar lenguaje comercial
- Enfoque técnico
- Escribir en lenguaje claro y sencillo, sin usar palabras complejas innecesarias
- Comenzar con la información más importante en **negrita**
- Usar párrafos cortos (máximo 2-3 oraciones)

3. Estructura:
- Usar ## para el título de la sección (formato Markdown)
- Solo usar UN solo elemento estructural SI ayuda a aclarar tu punto:
  * Ya sea una tabla enfocada comparando 2-3 elementos clave (usando sintaxis de tabla Markdown)
  * O una lista corta (3-5 elementos) usando la sintaxis adecuada de listas Markdown:
    - Usar `*` o `-` para listas desordenadas
    - Usar `1.` para listas ordenadas
    - Asegúrate de una correcta indentación y espaciado
- Terminar con ### Fuentes que referencian el material fuente abajo con formato:
  * Listar cada fuente con título, fecha y URL
  * Formato: `- Título : URL`

3. Enfoque de escritura:
- Incluir al menos un ejemplo específico o estudio de caso si está disponible
- Usar detalles concretos en lugar de declaraciones generales
- Hacer que cada palabra cuente
- No preámbulos antes de crear el contenido de la sección
- Centrarse en el punto más importante

4. Utiliza este material fuente obtenido de las búsquedas web para ayudar a escribir la sección:
{context}

5. Revisión de calidad:
- El formato debe ser Markdown
- Exactamente 150-200 palabras (excluyendo el título y las fuentes)
- Uso cuidadoso de solo UN solo elemento estructural (tabla o lista de viñetas) y solo si ayuda a aclarar tu punto
- Un ejemplo específico / estudio de caso si está disponible
- Comienza con la **negrita** del punto más importante
- Sin preámbulos antes de crear el contenido de la sección
- Fuentes citadas al final
- Si hay caracteres especiales en el texto, como el símbolo de dólar,
  asegúrate de escaparlos correctamente para la correcta representación, por ejemplo, $25.5 debe convertirse en \$25.5
"""

FINAL_SECTION_WRITER_PROMPT = """Eres un escritor técnico experto creando una sección que sintetiza información del resto del informe.

Título para la sección:
{section_title}

Tema para esta sección:
{section_topic}

Contenido disponible del informe con secciones ya completadas:
{context}

1. Enfoque específico de la sección:

Para Introducción:
- Usa # para el título del informe (formato Markdown)
- Límite de 50-100 palabras
- Escribe en lenguaje claro y sencillo
- Enfócate en la motivación central del informe en 1-2 párrafos
- Usa una narrativa clara para introducir el informe
- NO uses elementos estructurales (sin listas o tablas)
- No se necesita sección de fuentes

Para Conclusión/Resumen:
- Usa ## para el título de la sección (formato Markdown)
- Límite de 100-150 palabras
- Para informes comparativos:
    * Debe incluir una tabla de comparación enfocada usando sintaxis de tabla Markdown
    * La tabla debe destilar los conocimientos del informe
    * Mantén las entradas de la tabla claras y concisas
- Para informes no comparativos:
    * Solo usa UN solo elemento estructural SI ayuda a destilar los puntos tratados en el informe:
    * Ya sea una tabla enfocada comparando elementos presentes en el informe (usando sintaxis de tabla Markdown)
    * O una lista corta usando la sintaxis adecuada de listas Markdown:
      - Usa `*` o `-` para listas desordenadas
      - Usa `1.` para listas ordenadas
      - Asegúrate de una correcta indentación y espaciado
- Termina con pasos específicos siguientes o implicaciones
- No se necesita sección de fuentes

3. Enfoque de escritura:
- Usar detalles concretos en lugar de declaraciones generales
- Hacer que cada palabra cuente
- Centrarse en el punto más importante

4. Revisión de calidad:
- Para la introducción: límite de 50-100 palabras, usa # para el título del informe, sin elementos estructurales, sin sección de fuentes
- Para la conclusión: límite de 100-150 palabras, usa ## para el título de la sección, solo UN solo elemento estructural como máximo, sin sección de fuentes
- Formato Markdown
- No incluyas el conteo de palabras ni preámbulos en tu respuesta
- Si hay caracteres especiales en el texto, como el símbolo de dólar,
  asegúrate de escaparlos correctamente para la correcta representación, por ejemplo, $25.5 debe convertirse en \$25.5"""
