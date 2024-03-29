FROM python:3.9.18

ARG password="123456"

COPY backend /opt/weather_demo

RUN pip install -r /opt/weather_demo/requirements

WORKDIR /opt/weather_demo/

EXPOSE 8080

CMD ["gunicorn", "-c", "gunicorn.py", "main:app"]
