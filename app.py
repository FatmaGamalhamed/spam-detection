import joblib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


model = joblib.load("spam_detection_pipeline.pkl")

app = FastAPI(title="Spam Detection API")


# Allow the frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MessageRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "Spam Detection API is running"
    }


@app.post("/predict")
def predict(request: MessageRequest):

    prediction = model.predict(
        [request.message]
    )[0]

    probability = model.predict_proba(
        [request.message]
    )[0][1]

    result = (
        "Spam"
        if prediction == 1
        else "Ham"
    )

    return {
        "prediction": result,
        "spam_probability": round(
            float(probability),
            4
        )
    }