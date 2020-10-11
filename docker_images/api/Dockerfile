FROM tiangolo/uvicorn-gunicorn:python3.7

COPY ./requirements.txt /tmp/
RUN pip install --upgrade pip
RUN pip install --requirement /tmp/requirements.txt
WORKDIR /app
