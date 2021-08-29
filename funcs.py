def disp_value(y, logger=None):
    if logger is None:
        import logging

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(relativeCreated)6d %(threadName)s %(message)s",
        )
        logger = logging.getLogger(__name__)
    logger.info(f"Input is {y}")
