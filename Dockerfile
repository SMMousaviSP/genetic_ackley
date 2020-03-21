FROM python:3.6.10-slim

COPY ./requirements.txt /src/python/genetic_ackley/
RUN pip install -r /src/python/genetic_ackley/requirements.txt

COPY app /src/python/genetic_ackley/app/

CMD python -i /src/python/genetic_ackley/app/models/chromosome.py