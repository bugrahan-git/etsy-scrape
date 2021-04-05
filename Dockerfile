FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.8.0/wait /wait
RUN chmod +x /wait

COPY requirements.txt /app/

RUN pip install -r requirements.txt
COPY . /app/

CMD /wait
