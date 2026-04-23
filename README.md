# Weighted Contribution Index API

## Endpoint
POST /api/v1/weighted-contribution

## Description
Calculates overall all-rounder contribution using weighted scoring across batting, bowling, and fielding.

## Run Locally
pip install -r requirements.txt
uvicorn main:app --reload

## Input
JSON with batting, bowling, and fielding stats

## Output
Structured performance scores and impact label
