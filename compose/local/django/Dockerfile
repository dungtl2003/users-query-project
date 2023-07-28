# The image you are going to inherit your Dockerfile from
FROM python:3.10.6-alpine
# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1
ARG APP_HOME=/django_users_query_app/app
ARG ROOT_PROJECT=/django_users_query_app

ADD ./app $APP_HOME

COPY ./Pipfile ./Pipfile.lock $ROOT_PROJECT

COPY --chmod=771 ./compose/local/django/start /start

WORKDIR $ROOT_PROJECT

RUN pip install pipenv && \
    pipenv sync

WORKDIR $APP_HOME

EXPOSE 8000