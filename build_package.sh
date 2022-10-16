#!/bin/bash
poetry build
poetry run pip install -t target dist/*.whl
cd target && zip -r ../deployment-package.zip .
cd ../