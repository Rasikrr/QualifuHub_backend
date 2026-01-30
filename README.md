# QualifyHub MVP

## Tech Stack
- **FastAPI**: Web Framework
- **SQLModel**: ORM (SQLAlchemy + Pydantic)
- **PostgreSQL**: Database
- **OpenAI**: Matching Algorithm
- **Docker Compose**: For local DB setup

## Database Migrations

This project uses **Alembic** for database migrations.

1.  **Create a new migration** (after changing models):
    ```bash
    python -m alembic revision --autogenerate -m "Description of change"
    ```

2.  **Apply migrations**:
    ```bash
    python -m alembic upgrade head
    ```

## Getting Started

1. **Setup Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   Update `.env` with your `OPENAI_API_KEY` and `DATABASE_URL`.

3. **Start PostgreSQL**:
   ```bash
   docker-compose up -d
   ```

4. **Initialize Database**:
   ```bash
   python -m app.db.init_db
   ```

5. **Run the Application**:
   ```bash
   uvicorn app.main:app --reload
   ```

6. **API Documentation**:
   Once running, visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger UI.

## Features
- CRUD for Vacancies and CVs
- Skill verification endpoint
- Smart matching using OpenAI to rank candidates for a specific vacancy
