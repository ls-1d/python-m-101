# Use an official Python image from Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=development

# Set the working directory in the container
WORKDIR /app

# Copy the content of your local folder to the container's working directory
COPY . /app/

# Install the Python dependencies from your requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the Flask app port (default Flask port)
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
