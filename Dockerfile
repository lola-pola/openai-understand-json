FROM python:3.10-slim



# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update


# Set work directory
WORKDIR /app

# Copy project
COPY app .
COPY requirements.txt .


# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run server
CMD ["streamlit", "run" , "app.py","--server.port","80"]