import logging
import os
import sys

# this is to include backend dir in sys.path so that we can import from main project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from sqlalchemy import create_engine
from core.configs.env import get_settings

settings = get_settings()

databaseURI = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name_test}"

engine = create_engine(databaseURI, echo=True)


@pytest.fixture(autouse=True)
def suppress_sqlalchemy_logs():
    # Suppress SQLAlchemy logs by setting the log level to WARNING or higher
    logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.ERROR)
    logging.getLogger("sqlalchemy.dialects").setLevel(logging.ERROR)
