import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = Path(os.getenv("DATA_DIR", "../data"))
DATA_DIR.mkdir(parents=True, exist_ok=True)

class Config:
    """Base configuration"""
    APP_NAME = os.getenv("APP_NAME", "AI Secretary Platform")
    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", 8000))
    API_PREFIX = os.getenv("API_PREFIX", "/api")
    MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY", "")
    MINIMAX_MODEL = os.getenv("MINIMAX_MODEL", "minimax-2.7")
    DATA_DIR = DATA_DIR
    SESSION_TIMEOUT = int(os.getenv("SESSION_TIMEOUT", 3600))
    SCHEDULER_ENABLED = os.getenv("SCHEDULER_ENABLED", "True").lower() == "true"
    TIMEOUT_CHECK_INTERVAL = int(os.getenv("TIMEOUT_CHECK_INTERVAL", 5))

config = Config()
