#!/bin/bash

# all config is in the environment variables
set -a
source .env
set +a

# for small small collections
./bin/dump.sh
./bin/load.sh

# for large collections
poetry run python3 bin/main.py
