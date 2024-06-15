#!/bin/bash
set -e

# Set the working directory to the correct path
WORK_DIR="/var/jenkins_home/workspace/identidock/app"

if [ "$ENV" = "DEV" ]; then
    echo "Running Development Server"
    exec python "$WORK_DIR/identidock.py"
elif [ "$ENV" = "UNIT" ]; then
    echo "Running Unit test"
    exec python "$WORK_DIR/tests.py"
else
    echo "Running Production Server"
    exec uwsgi --http 0.0.0.0:9090 --wsgi-file "$WORK_DIR/identidock.py" --callable app --stats 0.0.0.0:9191
fi
