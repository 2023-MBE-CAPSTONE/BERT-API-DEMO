FROM amazon/aws-lambda-python:3.8
RUN pip install pipenv
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock
RUN pipenv install --dev --system --deploy
COPY ./src ./src/
COPY .env .env
CMD ["src.app.app.handler"]