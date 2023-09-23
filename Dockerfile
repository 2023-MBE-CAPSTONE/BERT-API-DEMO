FROM python:3.11
WORKDIR /bert-api-demo
RUN pip install pipenv
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock
RUN pipenv install 
COPY ./src ./src/
COPY .env .env
CMD ["pipenv", "run", "python", "./src/main.py"]