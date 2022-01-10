#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Loadbalancer debug application using flask and python3
# Copyright (C) RC30-popo 2022

from flask import Flask
from flask import request
import socket

PORT=5000
my_host = socket.gethostname()
my_ip = socket.gethostbyname(my_host)

app = Flask(__name__)

@app.route('/')
def hello():
    global myhost,my_ip
    mes = 'Hello World!!\n' + 'My Hostname='+my_host+',My IP='+my_ip+'\n'
    client_ip = request.remote_addr
    mes += 'Client IP='+client_ip + '\n'
    mes += '**Request Headers**\n'
    for header_key in request.headers.keys():
        mes += header_key + ':' + request.headers.get(header_key) + '\n'
    return mes

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=PORT)

