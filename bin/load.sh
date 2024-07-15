#!/usr/bin/sh

# upload all small collections
mongorestore --uri=$MONGO_NEW_URI --nsFrom="$MONGO_OLD_DB.*" --nsTo="$MONGO_NEW_DB.*"
