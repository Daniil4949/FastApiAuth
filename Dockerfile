# Pull base image
FROM python:3.10.6

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR .

# Install dependencies
RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system
COPY . .
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000
