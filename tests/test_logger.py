from utilities.logger import get_logger


logger = get_logger("TestLogger")


def test_logging():

    logger.debug("This is debug message")

    logger.info("Test started")

    logger.warning("This is a warning")

    logger.error("This is an error")

    logger.critical("This is a critical message")

    assert True