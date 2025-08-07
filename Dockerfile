FROM python:3.11

WORKDIR /

RUN pip install poetry


COPY pyproject.toml poetry.lock* ./

RUN poetry lock
RUN poetry install --no-root

COPY . .

EXPOSE 8012

CMD ["poetry", "run", "python", "main.py"]