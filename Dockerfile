FROM python:3.9
RUN apt-get update && \
    apt-get install -y python3-tk
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysql-connector-python

# Copy the rest of the application code to the container
COPY . .

 EXPOSE 8000

