import json

import requests

class huggingFace():
    def __init__(self,API_URL: str,API_TOKEN: str):
        self.API_URL = API_URL
        self.headers = {"Authorization": f"Bearer {API_TOKEN}"}
    
    def query(self,input_text: str) -> json:
        input_data = json.dumps(input_text)
        response = requests.request("POST",self.API_URL,headers=self.headers,data=input_data)
        return json.loads(response.content.decode("utf-8"))


