import os

from dotenv import load_dotenv

from src.models.hugging_face import huggingFace

'''
python -m tests.unit-tests.test_hugging_face 으로 실행 가능
'''
if __name__ == "__main__":
    load_dotenv(verbose=True)
    API_URL = os.getenv('HUGGING_FACE_API_URL')
    API_TOKEN = os.getenv('HUGGING_FACE_API_TOKEN')
    input_text = "3 년째 쓴 아이폰,"

    hf = huggingFace(API_URL,API_TOKEN)
    output_text = hf.query(input_text)
    print(output_text)


    
    












