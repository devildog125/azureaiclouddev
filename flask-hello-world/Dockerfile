# Use official Python slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY flask-hello-world/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
