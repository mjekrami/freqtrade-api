#!/bin/bash
VERSION=${GITHUB_SHA}
if docker ps -q -f name=freqtrade-api; then
    echo "Stopping and removing existing 'freqtrade-api' container..."
    docker stop freqtrade-api && docker rm freqtrade-api
else
    echo "'freqtrade-api' container is not running."
fi

echo "Starting a new 'freqtrade-api' container on port ${RUNNING_PORT}..."
docker run --name freqtrade-api --rm -v /var/run/docker.sock:/var/run/docker.sock -d -p ${RUNNING_PORT}:3000 freqtrade-api:${VERSION}

if [ $? -eq 0 ]; then
    echo "Container 'freqtrade-api' started successfully."
else
    echo "Failed to start the 'freqtrade-api' container."
fi
