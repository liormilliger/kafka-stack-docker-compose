# subscriber.Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the subscriber script to the container
COPY subscriber.py .

# Install the required packages
RUN pip install kafka-python

# Command to run the subscriber
CMD ["python", "subscriber.py"]
