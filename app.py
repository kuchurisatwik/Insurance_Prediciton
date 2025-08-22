from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from schemas import user_input
from models.predict import predict_output,MODEL_VERSION,model
from  schemas.prediction_response import PredictionResponse
 


app = FastAPI()
        

@app.get("/")
def Home():
    return {
        'FastAPI':'API is Woking'
    }


@app.get("/health")
def health_check():
    return {
        'status':'OK',
        'VERSION':MODEL_VERSION,
        'model_loaded':model is not None
    }


@app.post('/predict',response_model = PredictionResponse )
def predict_premium(data: user_input.UserInput):

    user_input = {
        'bmi':data.bmi,
        'age_group' : data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code = 200, content = {'response': prediction})
    except Exception as e:
        return JSONResponse(status_code = 500, content = str(e))