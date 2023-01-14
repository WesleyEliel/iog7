#!/bin/bash

# Stop execution if we have an error
>&2 echo "Built, Starting Server | Executing Command"
# Execute given other parameters (commands)
exec "$@"