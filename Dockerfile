FROM tiangolo/uvicorn-gunicorn:python3.9-slim

# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .