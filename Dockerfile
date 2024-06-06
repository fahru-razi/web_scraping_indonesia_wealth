FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY web_scraping/ web_scraping/
WORKDIR /app/web_scraping

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python", "run.py"]
