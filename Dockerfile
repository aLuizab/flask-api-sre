FROM python:3.8-alpine

COPY requirements.txt /requirements.txt

WORKDIR /

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]