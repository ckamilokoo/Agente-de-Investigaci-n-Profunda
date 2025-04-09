# Rutas para generaci�n de reportes
# app/routers/report_generation.py
from fastapi import APIRouter, HTTPException
from models.report import ReportStateInput, ReportStateOutput
from core.report_generation_logic import reporter_agent
from typing import Any

router = APIRouter()

@router.post("/generate_report/", response_model=ReportStateOutput)
async def generate_report(report_input: ReportStateInput) -> Any:
    try:
        result = await reporter_agent.ainvoke(report_input)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating report: {e}")