# Dockerfile Development

# pull the official docker image
FROM python:3.11.1-slim

# set work directory
WORKDIR /usr/src/app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

CMD [ "uvicorn" ,"app.main:app", "--host", "0.0.0.0", "--port","8000"]
