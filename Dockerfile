FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default command to run the API, can be overridden
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
