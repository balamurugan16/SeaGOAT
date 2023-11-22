FROM python:latest

WORKDIR /app

COPY . /app

RUN pip install poetry

RUN poetry install --no-interaction --no-ansi

EXPOSE 8000

CMD [ "poetry", "run", "python", "main.py" ]
