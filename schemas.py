from pydantic import BaseModel, Field

class PlayerInput(BaseModel):
    runs_scored: int = Field(ge=0)
    balls_faced: int = Field(ge=0)
    strike_rate: float = Field(ge=0)

    overs_bowled: float = Field(ge=0)
    runs_conceded: int = Field(ge=0)
    wickets_taken: int = Field(ge=0)

    catches: int = Field(ge=0)
    run_outs: int = Field(ge=0)
    stumpings: int = Field(ge=0)

class ContributionResponse(BaseModel):
    success: bool
    batting_score: float
    bowling_score: float
    fielding_score: float
    total_score: float
    impact: str
