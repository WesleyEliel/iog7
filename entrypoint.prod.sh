#!/bin/sh

# .docker/elasticsearch/wait-for-elascticsearch.sh
# .docker/elasticsearch/setup-elasticsearch.sh
# .docker/postgres/wait-for-postgres.sh

# python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"