from fastapi import FastAPI
from app.core.config import settings

from app.api.v1 import vacancies, cvs, dictionaries, matching

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/")
def root():
    return {"message": "Welcome to QualifyHub API"}

app.include_router(dictionaries.router, prefix=f"{settings.API_V1_STR}/dictionaries", tags=["Dictionaries"])
app.include_router(vacancies.router, prefix=f"{settings.API_V1_STR}/vacancies", tags=["Vacancies"])
app.include_router(cvs.router, prefix=f"{settings.API_V1_STR}/cvs", tags=["CVs"])
app.include_router(matching.router, prefix=settings.API_V1_STR, tags=["Matching"])
