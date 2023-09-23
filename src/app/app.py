from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "This is demo server for BERT !!!!"}
