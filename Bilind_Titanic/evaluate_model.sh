#!/usr/bin/env bash

export FILE_NAME_TEST=${1:-}
export MODEL_NAME=${2:-}

echo "Test file name is ${FILE_NAME_TEST}"
echo "Model name is ${MODEL_NAME}"

cd ./src/main/python

chmod +x evaluate_model.py
python evaluate_model.py

echo "Job Complete"
