import requests
from bs4 import BeautifulSoup

url = "http://43.200.87.239:5000"

class RandomForestDiagnosis:
    def request(self, ANIMAL: str, AREA: str, SYMPTOM1: str, SYMPTOM2: str):
        try:
            result = requests.post(url + "/predict",data={'a':ANIMAL,'b':AREA,'c':SYMPTOM1,'d':SYMPTOM2}).text
            startIdx = result.index("<h2>  </h2>")
            result = result[startIdx + 25:]
            endIdx = result.index("</h2>")
            result = result[:endIdx]

            message = ""
            if len(ANIMAL)==7:
                message += ANIMAL[0:3]
            else:
                message += ANIMAL
            if len(AREA)!=0:
                message += (" "+str(AREA))
            if len(AREA)!=0:
                message += (" "+str(SYMPTOM1))
            if len(AREA)!=0:
                message += (" "+str(SYMPTOM2))
            message += "와 관련된 질병은 다음과 같습니다.\n"
            return message + result
        except Exception:
            return self.sorry('그 질병은 알 수 없어요.')

    def sorry(self, text: str = None) -> str:
        if text is None:
            return "죄송합니다. 그건 알 수 없어요"
        else:
            return text

if __name__ == '__main__':
    diagnosis = RandomForestDiagnosis()
    print(diagnosis.request(ANIMAL='고양이',AREA='다리',SYMPTOM1='통증',SYMPTOM2='구토'))
