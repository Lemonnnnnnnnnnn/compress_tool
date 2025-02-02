import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def setup_logging():
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # 控制台输出
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # 文件日志
    logger.addHandler(console_handler) 