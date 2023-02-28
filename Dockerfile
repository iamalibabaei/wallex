FROM python:3.9-alpine

RUN mkdir /src

WORKDIR /src

ADD requirements.txt /src
RUN pip3 install -r requirements.txt

ADD . /src

CMD ["gunicorn", "-w 1", "-b", "0.0.0.0:8000", "src.infra.http.server:app"]