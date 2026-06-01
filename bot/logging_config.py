import logging
import os
def setup_logging():
    """Sets up a dual-destination logger writing to both standard output and a file."""
    log_dir="logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logger=logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-[%(filename)s:%(lineno)d]-%(message)s')
        file_handler=logging.FileHandler(os.path.join(log_dir,"bot.log"))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        console_handler=logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    return logger
logger=setup_logging()