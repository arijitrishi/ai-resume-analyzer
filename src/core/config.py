from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "mysql+pymysql://root:root@localhost/resume_analyzer"  # Update with your MySQL creds
    ml_model_path: str = "src/ml"  # Path to ML modules
    max_file_size: int = 5 * 1024 * 1024  # 5MB limit for PDFs

    class Config:
        env_file = ".env"  # Load from .env file for secrets

settings = Settings()