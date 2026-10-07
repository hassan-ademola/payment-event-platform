from fastapi import FastAPI

app = FastAPI(title="Payment Event Platform")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
