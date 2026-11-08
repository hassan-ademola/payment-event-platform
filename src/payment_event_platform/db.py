
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from payment_event_platform.settings import Settings

settings = Settings()

if not settings.database_url:
    raise ValueError("DATABASE_URL is not configured")

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(bind=engine)
