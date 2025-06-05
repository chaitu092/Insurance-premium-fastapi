from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, MODEL_VERSION, model
from schema.prediction_response import PredictionResponse
# Create the FastAPI app
app = FastAPI()

        
# human readable api
@app.get("/")
def home():
    return {'message': 'Insurance Premium Prediction API'}

#machine readable api
@app.get('/health')
def health_check():
    """checks status of API is working properly or not
     (This is useful when we deploy it in AWS cloud services like elastic search, kubernetes)
    """

    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None,
    }

@app.post("/predict", response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
                "bmi": data.bmi,
                "age_group": data.age_group,
                "lifestyle_status": data.lifestyle_status,
                "city_tier": data.city_tier,
                "income_lpa": data.income_lpa,
                "occupation": data.occupation,
            }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={"response": prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))