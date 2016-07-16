#!/usr/bin/env bash

export SERVER_USER=${1:-}
export SERVER_PASSWORD=${2:-}
export SERVER_HOST=${3:-}
export SERVER_DB_NAME=${4:-}
export TABLE_NAME=${5:-}
export TEST_PERCENT=${6:-}

echo "Server User is ${SERVER_USER}"
echo "Server Host is ${SERVER_HOST}"
echo "Server Database is ${SERVER_DB_NAME}"
echo "Database Table is ${TABLE_NAME}"

cd ./src/main/python

chmod +x prepare_data.py
python prepare_data.py

echo "Job Complete"