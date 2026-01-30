from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.domain import Vacancy, VacancySkill, VacancyBase, CategoryEnum
from pydantic import BaseModel

router = APIRouter()

class VacancyCreate(VacancyBase):
    required_skills: List[str]

class VacancyRead(VacancyBase):
    id: UUID
    status: str
    required_skills: List[str]

    @classmethod
    def from_orm_custom(cls, vacancy: Vacancy):
        return cls(
            id=vacancy.id,
            title=vacancy.title,
            description=vacancy.description,
            category=vacancy.category,
            salary_range=vacancy.salary_range,
            location=vacancy.location,
            status=vacancy.status.value,
            required_skills=[s.name for s in vacancy.required_skills]
        )

@router.post("/", response_model=VacancyRead, status_code=status.HTTP_201_CREATED)
def create_vacancy(vacancy_in: VacancyCreate, session: Session = Depends(get_session)):
    db_vacancy = Vacancy(
        title=vacancy_in.title,
        description=vacancy_in.description,
        category=vacancy_in.category,
        salary_range=vacancy_in.salary_range,
        location=vacancy_in.location
    )
    session.add(db_vacancy)
    session.commit()
    session.refresh(db_vacancy)
    
    for skill_name in vacancy_in.required_skills:
        skill = VacancySkill(name=skill_name, vacancy_id=db_vacancy.id)
        session.add(skill)
    
    session.commit()
    session.refresh(db_vacancy)
    return VacancyRead.from_orm_custom(db_vacancy)

@router.get("/", response_model=List[VacancyRead])
def list_vacancies(session: Session = Depends(get_session)):
    vacancies = session.exec(select(Vacancy)).all()
    return [VacancyRead.from_orm_custom(v) for v in vacancies]

@router.get("/{id}", response_model=VacancyRead)
def get_vacancy(id: UUID, session: Session = Depends(get_session)):
    vacancy = session.get(Vacancy, id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return VacancyRead.from_orm_custom(vacancy)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vacancy(id: UUID, session: Session = Depends(get_session)):
    vacancy = session.get(Vacancy, id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    session.delete(vacancy)
    session.commit()
    return None
