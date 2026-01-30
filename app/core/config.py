from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "QualifyHub"
    DATABASE_URL: str
    OPENAI_API_KEY: str = ""
    API_V1_STR: str = "/api/v1"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
