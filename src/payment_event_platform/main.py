import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from payment_event_platform.settings import Settings

settings = Settings()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(
        "application_started environment=%s",
        settings.environment,
    )

    yield

    logger.info("application_stopped")


app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
)


@app.get("/health")
def health() -> dict[str, str]:
    logger.info("health_check_completed")
    return {"status": "ok"}