FROM python:latest
WORKDIR /usr/src/desafio_datavisiooh
COPY ./requirements.txt .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install -r ./requirements.txt
COPY . .
EXPOSE 3000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:3000" ]

