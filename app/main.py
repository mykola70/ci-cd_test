"""FastAPI-приложение для демонстрации CI/CD пайплайна.

Предоставляет базовые эндпоинты для проверки работоспособности
приложения при локальном запуске и после деплоя.
"""
from fastapi import FastAPI

app = FastAPI(title="CI/CD Demo App", version="1.0.0")


@app.get("/")
async def root():
    """Корневой эндпоинт.

    Returns:
        dict: Приветственное сообщение и статус приложения.
    """
    return {"message": "Hello from CI/CD Demo App!", "status": "ok"}


@app.get("/health")
async def health():
    """Эндпоинт проверки состояния приложения (health check).

    Returns:
        dict: Статус "healthy" при нормальной работе сервиса.
    """
    return {"status": "healthy"}
