FROM python:3.11-slim
WORKDIR /app

COPY autogen/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY auth/ ./auth/
COPY autogen/service.py ./service.py
COPY autogen/tool.py ./tool.py

ENV PYTHONPATH=/app
EXPOSE 8011
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8011"]
