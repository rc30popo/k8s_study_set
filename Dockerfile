# Dockerfile for flask-hello application
# Copyright (C) 2022, RC30-popo


FROM ubuntu:18.04

EXPOSE 5000

RUN apt -y update
RUN apt -y upgrade
RUN apt -y install python3
RUN apt -y install python3-pip
RUN pip3 install flask


ENV APPDIR /flaskapp
RUN mkdir -p ${APPDIR}
COPY ./hello.py ${APPDIR}/hello.py
RUN chmod +x ${APPDIR}/hello.py
WORKDIR ${APPDIR}

ENTRYPOINT ["./hello.py" ]

