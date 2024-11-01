FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
