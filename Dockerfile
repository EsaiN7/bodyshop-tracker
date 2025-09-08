# Base image with Python 3.12
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=run
ENV FLASK_ENV=development

# Expose port Flask will run on
EXPOSE 5000

# Default command to run Flask
CMD ["flask", "run", "--host=0.0.0.0"]
