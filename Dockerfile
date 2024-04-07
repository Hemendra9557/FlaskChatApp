# Use an appropriate base image that includes Python
FROM python:3.11

# Copy the current directory contents into the container at /app
COPY . /app
# Set the working directory inside the container
WORKDIR /app



# Install any dependencies required by your Flask application
RUN pip install -r requirements.txt

# Expose port 5000 to allow external access to your application
EXPOSE $port

# Set the default command to run your Flask application
CMD gunicorn --workers=4  --bind 0.0.0.0:$port main:app
