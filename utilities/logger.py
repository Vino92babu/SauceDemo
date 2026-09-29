import logging
import os


def get_logger(name):

    log_folder = "logs"

    os.makedirs(
        log_folder,
        exist_ok=True
    )

    log_file = os.path.join(
        log_folder,
        "automation.log"
    )

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler(
            log_file
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            file_handler
        )

    return logger