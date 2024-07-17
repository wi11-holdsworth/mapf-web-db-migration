#!/bin/bash

# all config is in the environment variables
set -a
source .env
set +a

# we only want to dump small collections
# IFS=':' read -ra collections <<< "$MONGO_SMALL_COLLECTIONS"

# # dump all records from each collection
# for collection in "${collections[@]}"; do
#     mongodump --uri=$MONGO_OLD_URI --db=$MONGO_OLD_DB -c=$collection
# done

# upload all small collections
# mongorestore --uri=$MONGO_NEW_URI --nsFrom="$MONGO_OLD_DB.*" --nsTo="$MONGO_NEW_DB.*"

# for large collections
python3 run python3 bin/main.py
