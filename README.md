# CI/CD Demo Project

Учебный проект для демонстрации работы CI/CD с использованием GitHub Actions, Docker и автоматического деплоя.

## Структура проекта

- `app/main.py` - FastAPI приложение
- `requirements.txt` - зависимости Python
- `Dockerfile` - конфигурация Docker образа
- `.github/workflows/deploy.yml` - GitHub Actions workflow

## Настройка

### 1. GitHub Secrets

Для работы деплоя необходимо настроить следующие секреты в репозитории:
**Settings → Secrets and variables → Actions**

- `SSH_HOST` - IP адрес или домен сервера
- `SSH_USER` - имя пользователя для SSH подключения
- `SSH_PRIVATE_KEY` - приватный SSH ключ для доступа к серверу
- `SSH_PORT` (опционально) - порт SSH (по умолчанию 22)

### 2. Требования к серверу

- Установлен Docker
- Доступ по SSH с использованием приватного ключа
- Пользователь должен иметь права на выполнение Docker команд

## Workflow

Workflow автоматически запускается при push в ветку `main` и выполняет:

1. **Build and push** - сборка Docker образа и публикация в GitHub Container Registry (GHCR)
2. **Deploy** - деплой на сервер через SSH с автоматическим обновлением контейнера

## Использование GitFlow

- `main` - основная ветка для продакшн деплоя
- Разработка ведется в отдельных ветках (например, `develop` или `feature/*`)
- Слияние в `main` происходит через Pull Request
- После мержа в `main` автоматически запускается workflow деплоя

## Проверка работы

После коммита в `main`:
1. Проверьте вкладку **Actions** в GitHub - workflow должен завершиться успешно
2. Проверьте работу приложения: `curl http://your-server:8000/`
3. Проверьте health endpoint: `curl http://your-server:8000/health`
