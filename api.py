from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
import joblib
import uvicorn
import pandas as pd
import numpy as np

model=joblib.load('model.pkl')
ct=joblib.load('ct.pkl')

app = FastAPI()

class Item(BaseModel):
    Partner: bool
    SeniorCitizen: bool
    InternetService: Literal['DSL', 'Fiber optic', 'No']
    PaymentMethod: Literal['Mailed check','Bank transfer (automatic)','Credit card (automatic)','Electronic check']
    PaperlessBilling: bool
    MonthlyCharges: float=Field(gt=17, lt=150)
    StreamingMovies: bool
    DeviceProtection: bool
    Contract: Literal['Month-to-month','Two year','One year']
    tenure: int=Field( gt=0, le=100,description="tenure is in months")
    Dependents: bool


@app.get('/about')
def about():
    return {"message": "Telco Customer Churn Prediction API"}

@app.post("/predict")
def predict_churn(item: Item):
    input_df = pd.DataFrame([item.model_dump()])

    transformed_data = ct.transform(input_df)
    prob = model.predict_proba(transformed_data)[0][1] #probability of churn class
    custom_threshold = 0.5
    prediction = (prob>=custom_threshold).astype(int)

    # Probability of churn class (class 1)
    churn_probability = float(
        model.predict_proba(transformed_data)[0][1]
    ) * 100

    if churn_probability < 30:
        discount = "No discount"

    elif churn_probability < 50:
        discount = "Small discount"

    elif churn_probability < 70:
        discount = "Medium discount"

    else:
        discount = "Big discount"

    return {
        "churn": bool(prediction),
        "churn_probability": round(churn_probability, 2),
        "discount": discount
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)