from sqlalchemy import create_engine

from src.finagentos.config.settings import settings

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
)