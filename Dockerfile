FROM python:3.9.9

WORKDIR /usr/src
RUN apt-get update && apt-get install -y uvicorn
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8095