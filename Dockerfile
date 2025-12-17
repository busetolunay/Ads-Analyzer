FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# no need to specify CMD here since  docker-compose overrides it
#but as a fallback,  default to the API 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]