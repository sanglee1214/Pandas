#!/usr/bin/env bash

export FILE_NAME_TRAIN=${1:-}

echo "FILE_NAME_TRAIN is ${FILE_NAME_TRAIN}"

cd ./src/main/python

chmod +x build_model.py
python build_model.py

echo "Job Complete"
