FROM python:3.8-slim

# Install cron
RUN apt-get update && apt-get install -y cron

# Set working directory
WORKDIR /app

# Copy your application files and structure
COPY src/ /app/src/
COPY requirements.txt /app/
COPY .env /app/

# Install dependencies
RUN pip install -r requirements.txt

# Install additional system dependencies for psycopg2
RUN apt-get install -y libpq-dev gcc

# Create the cron job for lambda_function.py
RUN echo "*/15 * * * * cd /app && /usr/local/bin/python /app/src/lambda_function.py >> /var/log/cron.log 2>&1" > /etc/cron.d/weather-cron

# Give execution rights to the cron job
RUN chmod 0644 /etc/cron.d/weather-cron

# Apply cron job
RUN crontab /etc/cron.d/weather-cron

# Create the log file
RUN touch /var/log/cron.log

# Make sure your scripts are executable
RUN chmod +x /app/src/lambda_function.py
RUN chmod +x /app/src/data_mining_service.py

# Command to start cron
CMD ["cron", "-f"]