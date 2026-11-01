from fastapi import FastAPI

from payment_event_platform.settings import Settings

settings = Settings()
app = FastAPI(title=settings.app_name)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
