from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship

class CategoryEnum(str, Enum):
    Frontend = "Frontend"
    Backend = "Backend"
    Fullstack = "Fullstack"
    Mobile = "Mobile"
    DevOps = "DevOps"
    QA = "QA"
    DataScience = "DataScience"
    Design = "Design"

class ExperienceLevelEnum(str, Enum):
    Junior = "Junior"
    Mid = "Mid"
    Senior = "Senior"
    Lead = "Lead"

class VacancyStatusEnum(str, Enum):
    Open = "Open"
    Closed = "Closed"

class CVBase(SQLModel):
    full_name: str
    email: str
    summary: Optional[str] = None
    experience_level: ExperienceLevelEnum

class CV(CVBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    skills: List["CVSkill"] = Relationship(back_populates="cv")

class CVSkillBase(SQLModel):
    name: str
    is_verified: bool = Field(default=False)

class CVSkill(CVSkillBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cv_id: UUID = Field(foreign_key="cv.id")
    cv: CV = Relationship(back_populates="skills")

class VacancyBase(SQLModel):
    title: str
    description: Optional[str] = None
    category: CategoryEnum
    salary_range: Optional[str] = None
    location: Optional[str] = None

class Vacancy(VacancyBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    status: VacancyStatusEnum = Field(default=VacancyStatusEnum.Open)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    # We'll store required skills as a comma-separated string or a separate table
    # For MVP, let's use a separate table for searchability
    required_skills: List["VacancySkill"] = Relationship(back_populates="vacancy")

class VacancySkill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    vacancy_id: UUID = Field(foreign_key="vacancy.id")
    vacancy: Vacancy = Relationship(back_populates="required_skills")
