FROM python:3.8-slim-buster as build

# Set the working directory to /dockerapi
WORKDIR /app

# Copy the current directory contents into the container at /DockerAPI
ADD ./app /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define Environment Variables
ENV PATH=$PATH:/app/
ENV PYTHONPATH /app/

# Run the Application
CMD python app.py