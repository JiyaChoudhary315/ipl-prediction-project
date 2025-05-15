# Use Python base image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container to '/app'
WORKDIR /app

# Copy everything from your project folder into the container's working directory
COPY . /app

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for FastAPI (this is the default port for FastAPI)
EXPOSE 8000

# Start the FastAPI app using uvicorn when the container starts
CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
