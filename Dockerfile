FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip3 install -r req.txt

CMD dbt run 