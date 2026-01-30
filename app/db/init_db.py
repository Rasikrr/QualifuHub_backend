from sqlmodel import SQLModel
from app.db.session import engine
# Import models to ensure they are registered
from app.models.domain import CV, CVSkill, Vacancy, VacancySkill

def init_db():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
