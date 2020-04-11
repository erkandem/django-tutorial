#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

echo sleeping ten seconds
sleep 10

until PGPASSWORD=$POSTGRES_INITIAL_PASSWORD psql -h "$host" -U postgres -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

>&2 echo "Postgres is up - executing command"
exec $cmd
