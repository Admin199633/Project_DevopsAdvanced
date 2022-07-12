FROM python:latest
ENV PYTHONPATH /usr/src/app
WORKDIR /app
ADD producer.py /app
ADD requirements.txt /app
RUN pip install --requirement /app/requirements.txt
