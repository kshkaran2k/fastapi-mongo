import os
from app.config.default import DefaultConfig

class Config:
    DATABASE_URI = os.getenv('DATABASE_URI', DefaultConfig.DATABASE_URI)
    ENV = os.getenv('ENV', DefaultConfig.ENV)
    MODE = os.getenv('MODE', DefaultConfig.MODE)

