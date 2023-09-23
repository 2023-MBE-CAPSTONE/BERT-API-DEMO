import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from fastapi import FastAPI
from dotenv import load_dotenv

from src.models.hugging_face import huggingFace

load_dotenv(verbose=True)
app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "This is demo server for BERT !!!!"}

@app.post("/predict/bert/")
async def predict_bert(input_message: str):
    BERT_API_URL = os.getenv('HUGGING_FACE_API_URL')
    BERT_API_TOKEN = os.getenv('HUGGING_FACE_API_TOKEN')
    hf = huggingFace(BERT_API_URL,BERT_API_TOKEN)
    output_text = hf.query(input_message)
    return output_text