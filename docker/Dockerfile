FROM python:3.14
ENV TZ="Europe/Brussels"
RUN date

WORKDIR /usr/src/app

COPY ../requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

