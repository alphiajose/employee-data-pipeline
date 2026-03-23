#!/bin/bash

echo "Starting pipeline at $(date)" >> pipeline.log

# Activate virtual environment
source venv/bin/activate

# Step 1: Download data
./download.sh >> pipeline.log 2>&1

# Step 2: Process data
python3 process.py >> pipeline.log 2>&1

echo "Pipeline completed at $(date)" >> pipeline.log
