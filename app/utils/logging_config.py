import logging
from logging.handlers import RotatingFileHandler

from app.config import LOG_FOLDER

def setup_logging():
    
    log_file = LOG_FOLDER / "app.log"
    
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s | %(name)s | %(message)s"
    )
    
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 *1024,
        backupCount=5
    )
    
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    
    console_handler = logging.StreamHandler()
    
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            file_handler,
            console_handler
        ]
    )