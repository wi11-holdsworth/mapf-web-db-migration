# mapf-web-db-migration-bin
A set of scripts for converting existing non-encoded data into run-length encoded data given read access to one database and write access to another of a specific configuration

## `.env` template
```bash
MONGO_OLD_URI=$SECRET
MONGO_OLD_DB=test
MONGO_NEW_URI=$SECRET
MONGO_NEW_DB=MAPF
MONGO_SMALL_COLLECTIONS="algorithms:maps:scenarios:submissions:users"
MONGO_LARGE_COLLECTIONS="instances:solution_paths"
```
