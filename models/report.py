# Modelos Pydantic para reportes
# app/models/report.py
from pydantic import BaseModel, Field
from typing import List, Optional
from typing_extensions import TypedDict
import operator
from typing import Annotated

class Section(BaseModel):
    name: str = Field(description="...")
    description: str = Field(description="...")
    research: bool = Field(description="...")
    content: str = Field(description="...")

class Sections(BaseModel):
    sections: List[Section] = Field(description="...")

class SearchQuery(BaseModel):
    search_query: Optional[str] = Field(None, description="...")

class Queries(BaseModel):
    queries: List[SearchQuery] = Field(description="...")

class ReportStateInput(TypedDict):
    topic: str

class ReportStateOutput(TypedDict):
    final_report: str

class ReportState(TypedDict):
    topic: str
    sections: list[Section]
    completed_sections: Annotated[list, operator.add]
    report_sections_from_research: str
    final_report: str

class SectionState(TypedDict):
    section: Section
    search_queries: list[SearchQuery]
    source_str: str
    report_sections_from_research: str
    completed_sections: list[Section]

class SectionOutputState(TypedDict):
    completed_sections: list[Section]