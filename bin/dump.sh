#!/usr/bin/sh

# we only want to dump small collections
IFS=':' read -ra collections <<< "$MONGO_SMALL_COLLECTIONS"

# dump all records from each collection
for collection in "${collections[@]}"; do
    mongodump --uri=$MONGO_OLD_URI --authenticationDatabase=admin --db=$MONGO_OLD_DB -c=$collection
done
