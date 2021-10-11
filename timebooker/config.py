from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str
    admin_email: str
    sqlalchemy_database_url: str

    class Config:
        env_file = '.env'
