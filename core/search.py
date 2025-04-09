# app/core/search.py

from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
import asyncio
from typing import List, Dict, Union, Any
from dataclasses import asdict, dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class SearchQuery:
    search_query: str
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

# Inicializa el wrapper de Tavily
tavily_search = TavilySearchAPIWrapper()

async def run_search_queries(
    search_queries: List[Union[str, SearchQuery]],
    num_results: int = 5,
    include_raw_content: bool = False
) -> List[Dict]:
    search_tasks = []

    for query in search_queries:
        # Asegura que sea una cadena
        query_str = query.search_query if isinstance(query, SearchQuery) else str(query)
        try:
            # Crea la tarea asíncrona
            search_tasks.append(
                tavily_search.raw_results_async(
                    query=query_str,
                    max_results=num_results,
                    search_depth='advanced',
                    include_answer=False,
                    include_raw_content=include_raw_content
                )
            )
        except Exception as e:
            print(f"Error creating search task for query '{query_str}': {e}")
            continue

    # Ejecuta todas las tareas en paralelo
    try:
        if not search_tasks:
            return []

        search_docs = await asyncio.gather(*search_tasks, return_exceptions=True)

        # Filtra excepciones
        valid_results = [
            doc for doc in search_docs if not isinstance(doc, Exception)
        ]
        return valid_results

    except Exception as e:
        print(f"Error during search queries: {e}")
        return []
