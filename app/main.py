from fastapi import FastAPI

app = FastAPI(title="CI/CD Demo App", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Hello from CI/CD Demo App!", "status": "ok"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
