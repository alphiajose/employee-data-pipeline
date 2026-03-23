# Employee Data Pipeline

This project automates the process of downloading, cleaning, and analyzing employee data.

## Features
- Download employee data using Bash script
- Clean data using Python (Pandas)
- Convert CSV to JSON
- Generate summary statistics
- Logging of pipeline execution
- Automated using cron

## Files
- download.sh → Downloads data
- process.py → Cleans and processes data
- run_pipeline.sh → Runs the full pipeline
- pipeline.log → Logs execution
- output.json → Final processed data
- summary.json → Summary statistics

## How to Run

```bash
./run_pipeline.sh
