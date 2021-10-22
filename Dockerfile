FROM python:3.9-slim-bullseye as build-image
ENV APP_HOME /app
WORKDIR $APP_HOME

RUN python -m venv ./opt/venv
# Make sure we use the virtualenv:
ENV PATH="./opt/venv/bin:$PATH"

COPY requirements/production.txt .
RUN pip install -r production.txt

FROM python:3.9-slim-bullseye as run-image

ENV APP_HOME /app
ARG UNAME=prod
ARG UID=500
ARG GID=500

WORKDIR $APP_HOME

RUN groupadd -g $GID -o $UNAME
RUN useradd -u $UID -g $GID -o $UNAME

RUN apt-get update && apt-get -y upgrade

USER $UNAME

COPY --chown=$UNAME:$UNAME --from=build-image $APP_HOME/opt/venv ./opt/venv

COPY micro ./micro
COPY app.py .

# Make sure we use the virtualenv:
ENV PATH="./opt/venv/bin:$PATH"

CMD ["gunicorn", \
    "--preload", \
    "--bind", "0.0.0.0:8080", \
    "--workers=5", "--threads=2", "--worker-class=gthread", \
    "--log-file=-", \
    "app:app"]
