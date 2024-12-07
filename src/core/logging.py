# rita/core/logging.py

import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

def setup_logging(log_dir: str = "logs"):
    # Create logs directory if it doesn't exist
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    
    # Configure root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Console handler with detailed formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)
    
    # File handler for persistent logs
    file_handler = RotatingFileHandler(
        f"{log_dir}/rita.log",
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)
    
    # Create separate logger for Ollama integration
    ollama_logger = logging.getLogger('rita.ollama')
    ollama_file_handler = RotatingFileHandler(
        f"{log_dir}/ollama_integration.log",
        maxBytes=10485760,
        backupCount=5
    )
    ollama_file_handler.setFormatter(file_format)
    ollama_logger.addHandler(ollama_file_handler)
    
    return logger

# Usage example in main FastAPI app
def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
