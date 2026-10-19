from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_ECHO: bool = False
    
    REDIS_HOST: str
    REDIS_PORT: int
    

    @property
    def async_database_url(self) -> str:
        """Динамически собирает строку подключения для асинхронного движка SQLAlchemy"""
        return (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


# Создаем экземпляр настроек для импорта в другие модули проекта
settings = Settings()