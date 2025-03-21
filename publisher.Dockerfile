# publisher.Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the publisher script to the container
COPY publisher.py .

# Install the required packages
RUN pip install kafka-python schedule

# Command to run the publisher
CMD ["python", "publisher.py"]
