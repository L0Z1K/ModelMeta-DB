from logging import getLogger

from src.db.database import Base

logger = getLogger(__name__)


def initialize_table(engine, checkfirst: bool = True):
    logger.info("Initialize tables")
    Base.metadata.create_all(engine, checkfirst=checkfirst)
