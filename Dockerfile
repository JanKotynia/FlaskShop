FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV SQLALCHEMY_DATABASE_URI=sqlite:///shop.db
ENV SECRET_KEY=changemeinprod!

EXPOSE 5000

CMD python db_sql_querry.py && python run.py
