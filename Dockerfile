FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \ PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY pyproject.toml README.md uv.lock ./
COPY src ./src

RUN pip install --upgrade pip \
    && pip install .

CMD ["python", "-m", "tick_telegram_bot.bot"]