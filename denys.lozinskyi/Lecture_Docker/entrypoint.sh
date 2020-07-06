#!/bin/bash

cd /app/src/server/
python3 simple-app-v2.py &

cd /app/
pytest -v > /app/test/logs/session_logs
