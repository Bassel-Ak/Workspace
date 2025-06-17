import logging
import os
from datetime import datetime

def setup_logger(name="credit_note_logger", log_dir="logs", debug=False):
    os.makedirs(log_dir, exist_ok=True)
    log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
    log_path = os.path.join(log_dir, log_filename)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Remove previous handlers to avoid duplicate logs
    logger.handlers.clear()

    # Set levels based on debug flag
    log_level = logging.DEBUG if debug else logging.INFO

    # File handler
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(log_level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    formatter = logging.Formatter('[%(levelname)s] %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
