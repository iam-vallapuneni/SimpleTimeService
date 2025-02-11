# Use a lightweight base image
FROM python:3.9-slim

# Set a non-root user
RUN useradd -m appuser
USER appuser

# Set working directory
WORKDIR /app

# Copy files and install dependencies
COPY . .
RUN pip install flask

# Expose the port and start the app
EXPOSE 5000
CMD ["python", "server.py"]
