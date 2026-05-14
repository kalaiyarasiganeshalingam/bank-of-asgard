FROM python:3.11-slim
WORKDIR /app

COPY strands/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY auth/ ./auth/
COPY strands/service.py ./service.py
COPY strands/tool.py ./tool.py

ENV PYTHONPATH=/app
EXPOSE 8011
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8011"]
