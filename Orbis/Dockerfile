FROM python:3.12-slim AS build

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir gunicorn

COPY requirements/dev.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY SharedBackend/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

FROM python:3.12-slim AS runtime

WORKDIR /src

COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

COPY --from=build /src /src
COPY app app
COPY SharedBackend SharedBackend
COPY alembic.ini alembic.ini
COPY migrations migrations
ENV PYTHONPATH=/src/app/:/src/SharedBackend/src/

RUN alembic revision --autogenerate
RUN alembic upgrade heads

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
