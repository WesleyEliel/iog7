
# pull official base image
FROM python:3.8

RUN mkdir /usr/src/app/
RUN mkdir /usr/src/app/static/
RUN mkdir /usr/src/app/static/static_files
RUN mkdir /usr/src/app/static/medias

# set work directory
WORKDIR /usr/src/app



# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install apt-utils && apt install -y netcat

RUN apt-get update && apt-get install apt-utils && apt-get -y dist-upgrade && apt-get install gettext \
    && apt-get install -y libsqlite3-mod-spatialite binutils libproj-dev gdal-bin python3-gdal \
    && apt-get install -y --no-install-recommends postgresql-client && apt-get install zbar-tools -y \
    && apt-get install libzbar-dev -y \
    && rm -rf /var/lib/apt/lists/*
     
# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv

COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install --skip-lock --system --dev


# copy project
COPY . /usr/src/app/

# add access
RUN chmod +x ./entrypoint.prod.sh && chmod +x ./entrypoint.sh


RUN ls -la

EXPOSE 8000

ENTRYPOINT [ "./entrypoint.prod.sh" ]

# ENTRYPOINT [ "./entrypoint.prod.sh" ]