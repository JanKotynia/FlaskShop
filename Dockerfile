FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN python db_sql_querry.py

EXPOSE 5000

# Uruchom aplikację
CMD ["flask", "run"]
