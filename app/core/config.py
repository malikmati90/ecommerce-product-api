from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    TITLE: str = "E-Commerce Product API"

    POSTGRES_USER: str = "root_user"
    POSTGRES_PASSWORD: str = "admin9090"
    POSTGRES_DB: str = "ecommerce_db"
    POSTGRES_HOST: str = "postgres_db"
    POSTGRES_PORT: int = 5432

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
