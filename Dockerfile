FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install requirements.txt

COPY . .

RUN python db_sql_querry.py

ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
