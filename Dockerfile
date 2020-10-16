FROM python:3.8-alpine

MAINTAINER Ana Luiza

COPY requirements.txt /requirements.txt

WORKDIR /

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]