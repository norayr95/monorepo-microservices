from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
class Settings(BaseSettings):
    app_name: str
    debug: bool = False
    class Config(SettingsConfigDict):
        env_file = f'{BASE_DIR}/.env'
        extra = "allow"



settings = Settings()

print(settings.debug)