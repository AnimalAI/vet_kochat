# 라이브러리 import
import requests
import pprint
import json

def test_kochat():
    url = 'http://127.0.0.1:8080/request_chat/gusdnd852/고양이 간식 구토'
    response = requests.get(url)
    contents = response.text
    print(contents)

if __name__ == "__main__":
    test_kochat()
