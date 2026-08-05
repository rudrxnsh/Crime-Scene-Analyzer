import os
from pathlib import Path 

# =====================================================
# BASE DIRECTORY
# =====================================================

# Crime-Scene-Analyzer/
BASE_DIR = Path(__file__).resolve().parent.parent


# =====================================================
# PROJECT DIRECTORIES
# =====================================================

UPLOAD_FOLDER = BASE_DIR / "uploads"
OUTPUT_FOLDER = BASE_DIR / "outputs"
REPORT_FOLDER = BASE_DIR / "reports"
LOG_FOLDER = BASE_DIR / "logs"
MODEL_FOLDER = BASE_DIR / "models"
DATABASE_FOLDER = BASE_DIR / "database"
SAMPLE_VIDEO_FOLDER = BASE_DIR / "sample_videos"


# =====================================================
# APPLICATION SETTINGS
# =====================================================

SECRET_KEY = os.getenv("SECRET_KEY", "crime-scene-analyzer-dev")

DEBUG = os.getenv("FLASK_DEBUG","True") == "True"

MAX_CONTENT_LENGTH = 100 * 1024 * 1024 # 100 MB


# =====================================================
# DATABASE 
# =====================================================

DATABASE_PATH = DATABASE_FOLDER / "crime_scene.db"


# =====================================================
# ALLOWED FILE TYPES
# =====================================================

ALLOWED_EXTENSIONS = {
    "mp4",
    "avi",
    "mov",
    "mkv",
    "mpeg",
    "wmv"
}


# =====================================================
# CREATE REQUIRED DIRECTORIES
# =====================================================

REQUIRED_DIRECTORIES = [
    UPLOAD_FOLDER,
    OUTPUT_FOLDER,
    REPORT_FOLDER,
    LOG_FOLDER,
    MODEL_FOLDER,
    DATABASE_FOLDER,
    SAMPLE_VIDEO_FOLDER,
]

for directory in REQUIRED_DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)