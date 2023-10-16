FROM python:3.10.5-slim-buster

WORKDIR /app

COPY req.txt req.txt

RUN pip install -r /app/req.txt

COPY . .

EXPOSE 80

CMD ["python", "./app.py"]