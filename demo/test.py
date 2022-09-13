# 라이브러리 import
import requests
import pprint
import json

def test_kochat():
    url = 'http://127.0.0.1:8080/request_chat/gusdnd852/고양이 간식 구토'
    response = requests.get(url)
    contents = response.text
    print(contents)

def test_ml():
    url = 'http://43.200.87.239:5000/predict'
    response = requests.get(url)
    contents = response.text
    print(contents)

test_kochat()
