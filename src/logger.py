import logging
import sys

class ColorFormatter(logging.Formatter):
    COLORS = {
        'INFO': '\033[32m',
        'WARNING': '\033[33m',
        'ERROR': '\033[31m'
    }
    RESET = '\033[0m'

    def format(self, record):
        color = self.COLORS.get(record.levelname, '')
        record.levelname = f"{color}{record.levelname}{self.RESET}"
        return super().format(record)

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.handlers = []

    ch = logging.StreamHandler(sys.stdout)
    formatter = ColorFormatter('[%(levelname)s] %(name)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger

if __name__ == "__main__":
    logger = setup_logger(__name__)
    logger.info("Pipeline started")
    logger.warning("Warning message")
    logger.error("Error occurred")


print("PR test change")