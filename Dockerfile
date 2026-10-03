FROM python:3.12-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
COPY webapp/requirements.lock /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY webapp /app/webapp
ENV DATABASE_PATH=/data/knowledge.sqlite
EXPOSE 8000
CMD ["sh", "-c", "exec uvicorn webapp.main:app --host 0.0.0.0 --port ${PORT:-8000} --no-access-log"]
