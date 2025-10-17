import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    PROJECT_NAME = "Pattern-Based Data Representation System"
    VERSION = "1.0.0"
    UPLOAD_DIR = os.getenv("UPLOAD_DIR", "data/uploads")
    HOST = "0.0.0.0"
    PORT = int(os.getenv("PORT", 8000))
settings = Settings()
