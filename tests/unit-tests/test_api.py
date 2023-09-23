import json

from fastapi.testclient import TestClient

from src.app.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")

    assert response.status_code == 200

    response_json = response.json()
    assert "msg" in response_json  
    assert response_json["msg"] == "This is demo server for BERT !!!!"

def test_predict_bert():
    input_text = "3년 째 쓴, 아이폰"
    input_json = {"input_message": input_text}

    response = client.post("/predict/bert/",json=input_json,)
    assert response.status_code == 200
    response_json = response.json().pop()
    assert "generated_text" in response_json
    

# Run the test function
if __name__ == "__main__":
    test_predict_bert()



