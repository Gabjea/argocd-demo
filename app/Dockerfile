FROM python:3.11-slim

WORKDIR /project

COPY app/requirements.txt ./app/
RUN pip install --no-cache-dir -r app/requirements.txt

COPY app/ ./app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]