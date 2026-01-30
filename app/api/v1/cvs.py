from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.domain import CV, CVSkill, CVBase, ExperienceLevelEnum
from pydantic import BaseModel

router = APIRouter()

class SkillRead(BaseModel):
    name: str
    is_verified: bool

class CVCreate(CVBase):
    skills: List[str]

class CVRead(CVBase):
    id: UUID
    skills: List[SkillRead]

    @classmethod
    def from_orm_custom(cls, cv: CV):
        return cls(
            id=cv.id,
            full_name=cv.full_name,
            email=cv.email,
            summary=cv.summary,
            experience_level=cv.experience_level,
            skills=[SkillRead(name=s.name, is_verified=s.is_verified) for s in cv.skills]
        )

@router.post("/", response_model=CVRead, status_code=status.HTTP_201_CREATED)
def create_cv(cv_in: CVCreate, session: Session = Depends(get_session)):
    db_cv = CV(
        full_name=cv_in.full_name,
        email=cv_in.email,
        summary=cv_in.summary,
        experience_level=cv_in.experience_level
    )
    session.add(db_cv)
    session.commit()
    session.refresh(db_cv)
    
    for skill_name in cv_in.skills:
        skill = CVSkill(name=skill_name, cv_id=db_cv.id)
        session.add(skill)
    
    session.commit()
    session.refresh(db_cv)
    return CVRead.from_orm_custom(db_cv)

@router.get("/", response_model=List[CVRead])
def list_cvs(session: Session = Depends(get_session)):
    cvs = session.exec(select(CV)).all()
    return [CVRead.from_orm_custom(c) for c in cvs]

@router.get("/{id}", response_model=CVRead)
def get_cv(id: UUID, session: Session = Depends(get_session)):
    cv = session.get(CV, id)
    if not cv:
        raise HTTPException(status_code=404, detail="CV not found")
    return CVRead.from_orm_custom(cv)

class VerifySkillInput(BaseModel):
    verified: bool

@router.patch("/{cvId}/skills/{skillName}/verify", response_model=CVRead)
def verify_skill(cvId: UUID, skillName: str, input_data: VerifySkillInput, session: Session = Depends(get_session)):
    cv = session.get(CV, cvId)
    if not cv:
        raise HTTPException(status_code=404, detail="CV not found")
    
    skill = next((s for s in cv.skills if s.name.lower() == skillName.lower()), None)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found for this CV")
    
    skill.is_verified = input_data.verified
    session.add(skill)
    session.commit()
    session.refresh(cv)
    return CVRead.from_orm_custom(cv)
