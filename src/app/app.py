import os,sys

from mangum import Mangum
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi import Body
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from src.models.hugging_face import huggingFace

load_dotenv(verbose=True)
app = FastAPI()
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
) 

@app.get("/")
async def root():
    return {"msg": "This is demo server for BERT !!!!"}

@app.post("/predict/bert/")
async def predict_bert(input_message: str = Body(..., embed=True)):
    BERT_API_URL = os.getenv('HUGGING_FACE_API_URL')
    BERT_API_TOKEN = os.getenv('HUGGING_FACE_API_TOKEN')
    hf = huggingFace(BERT_API_URL,BERT_API_TOKEN)
    output_text = hf.query(input_message)
    return output_text

@app.get("/{text}")
async def predict_bert_get(text: str):
    BERT_API_URL = os.getenv('HUGGING_FACE_API_URL')
    BERT_API_TOKEN = os.getenv('HUGGING_FACE_API_TOKEN')
    hf = huggingFace(BERT_API_URL,BERT_API_TOKEN)
    output_text = hf.query(text)
    return output_text

handler = Mangum(app)