import os
import json

import requests
from dotenv import load_dotenv


def query(payload,api_url,headers):
    data = json.dumps(payload)
    response = requests.request("POST", api_url, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

if __name__ == "__main__":
    load_dotenv(verbose=True)
    API_URL = os.getenv('HUGGING_FACE_API_URL')
    API_TOKEN = os.getenv('HUGGING_FACE_API_TOKEN')
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    
    input_text = "3 년째 쓴 아이폰,"
    data = query(input_text,API_URL,headers)
    print(data)


    
    












