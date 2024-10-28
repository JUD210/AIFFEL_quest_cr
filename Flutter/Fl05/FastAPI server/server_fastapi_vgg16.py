import uvicorn   # pip install uvicorn
from fastapi import FastAPI, HTTPException   # pip install fastapi
from fastapi.middleware.cors import CORSMiddleware
import vgg16_prediction_model
import logging

# Create the FastAPI application
app = FastAPI()

# CORS configuration
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the model once
try:
    vgg16_model = vgg16_prediction_model.load_model()
except Exception as e:
    logger.error("Failed to load model: %s", e)
    raise

# A simple example of a GET request
@app.get("/")
async def read_root():
    logger.info("Root URL was requested")
    return "VGG16 모델을 사용하는 API를 만들었습니다."

""" 기존 가이드라인에 있던 코드
@app.get('/sample')
async def sample_prediction():
    try:
        result = await vgg16_prediction_model.prediction_model(vgg16_model)
        logger.info("Prediction was requested and done")
        return result
    except Exception as e:
        logger.error("Prediction failed: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
"""

@app.get('/predict_class')
async def predict_class(image_path = './sample_data/jellyfish.jpg'):
    try:
        result = await vgg16_prediction_model.prediction_model(vgg16_model, image_path)
        predicted_class = result["predicted_label"]
        logger.info("Prediction class was requested and done")
        return {"predicted_label": predicted_class}
    except Exception as e:
        logger.error("Prediction failed: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get('/predict_probability')
async def predict_probability(image_path = './sample_data/jellyfish.jpg'):
    try:
        result = await vgg16_prediction_model.prediction_model(vgg16_model, image_path)
        prediction_score = result["prediction_score"]
        logger.info("Prediction score was requested and done")
        return {"prediction_score": prediction_score}
    except Exception as e:
        logger.error("Prediction failed: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Run the server
if __name__ == "__main__":
    uvicorn.run("server_fastapi_vgg16:app",
            reload=True,   # Reload the server when code changes
            host="127.0.0.1",   # Listen on localhost
            port=8080,   # Listen on port 8080
            log_level="info"   # Log level
            )