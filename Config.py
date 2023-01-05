from pydantic import BaseSettings


class Settings(BaseSettings):
    app_port: int

    class Config:
        env_file = "example.env"
