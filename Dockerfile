FROM python:3.10

RUN apt-get update && apt-get install -y libcups2-dev gcc

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","main.py"]