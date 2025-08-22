from typing import Annotated, Dict
from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    predicted_category: Annotated[str, Field(
        description="The predicted insurance premium category",
        examples=["High"]  # 👈 note: in v2 it's `examples`, not `example`
    )]

    confidence: Annotated[float, Field(
        description="Model's confidence score (0–1)",
        examples=[0.8432]
    )]

    class_probabilities: Annotated[Dict[str, float], Field(
        description="Probability distribution across all possible classes",
        examples=[{"Low": 0.01, "Medium": 0.15, "High": 0.84}]
    )]
