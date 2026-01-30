from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.domain import Vacancy, CV
from app.api.v1.cvs import CVRead
from app.services.matching_service import rank_cvs_for_vacancy

router = APIRouter()

@router.get("/vacancies/{id}/matches", response_model=List[CVRead])
def get_vacancy_matches(id: UUID, session: Session = Depends(get_session)):
    vacancy = session.get(Vacancy, id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    
    # Get all CVs (in a real app we would filter by category first for efficiency)
    cvs = session.exec(select(CV)).all()
    
    ranked_cvs = rank_cvs_for_vacancy(vacancy, cvs)
    
    return [CVRead.from_orm_custom(c) for c in ranked_cvs]
