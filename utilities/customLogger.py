import logging
import time


class LogGenerator:
    @staticmethod
    def log_generator(log_file=""):
        if not log_file:
            log_file = ".\\Logs\\log_" + time.strftime("%Y%m%d_%H%M%S") + ".log"
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # Create a file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a formatter and set it for both handlers
        format_str = "[%(asctime)s %(levelname)-s %(threadName)s %(filename)s:%(lineno)d] %(message)s"
        formatter = logging.Formatter(format_str)
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
