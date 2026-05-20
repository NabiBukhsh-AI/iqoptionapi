"""IQ Option API — unofficial Python wrapper, community maintained."""

import logging

from iqoptionapi.stable_api import IQ_Option

__all__ = ["IQ_Option"]


def _prepare_logging():
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.NullHandler())
    logging.getLogger("websocket").addHandler(logging.NullHandler())


_prepare_logging()
