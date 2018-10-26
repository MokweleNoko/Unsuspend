From python:3.7.0

# Set the working directory to /app
WORKDIR /docker

# Copy the current directory contents into the container at /app
ADD . /docker

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80


# Run app.py when the container launches
CMD ["python", "app.py"]
