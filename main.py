from fastapi import FastAPI, HTTPException
from schemas import PlayerInput, ContributionResponse
from services import calculate_contribution
import logging

app = FastAPI(title="Weighted Contribution Index API", version="1.0")

logging.basicConfig(level=logging.INFO)

@app.post("/api/v1/weighted-contribution", response_model=ContributionResponse)
def weighted_contribution(data: PlayerInput):
    try:
        logging.info("Weighted contribution request received")
        return calculate_contribution(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
