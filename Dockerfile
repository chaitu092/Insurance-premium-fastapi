# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy files
COPY . .

# expose application port
EXPOSE 8000

# Run cpmmand to start FastAPI application
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port" ,"8000"]
