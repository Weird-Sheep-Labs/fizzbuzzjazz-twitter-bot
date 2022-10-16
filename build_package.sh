#!/bin/bash
poetry build
poetry run pip install -t target dist/*.whl
cd target && zip -q -r ../deployment-package.zip .
cd ../