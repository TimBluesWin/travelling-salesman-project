FROM python:bookworm


ENV PYTHONUNBUFFERED=1

WORKDIR /tsp-backend

COPY . .

RUN pip install -r requirements.txt
ENV DJANGO_SETTINGS_MODULE=backend.settings
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 setupData.py

EXPOSE 8000
