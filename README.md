# Security-testable Flask API

## How to add a new entity
1. Add an entity to the models folder
2. Add an namespace within the apis folder

## How to generate the certificates?
This generates a certificate with 10 years (3650 days) validity. Just in case, this is the command I used:

> $ openssl req -x509 -newkey rsa:4096 -nodes -out api_cert.pem -keyout api_key.pem -days 3650

## Running in a Production Server

> $ gunicorn --certfile certs/api_cert.pem --keyfile certs/api_key.pem -b 0.0.0.0:5000 app:app

## Start the Database and API

> $ docker-compose build && docker-compose up

## Pending
- Organize configurations independently

This API is available at: http://127.0.0.1:5000/

A Postman collection is also included