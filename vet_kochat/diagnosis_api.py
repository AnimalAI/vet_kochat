import requests

url = "http://43.200.87.239:5000"

class RandomForestDiagnosis:
    def request(self, ANIMAL: str, AREA: str, SYMPTOM1: str, SYMPTOM2: str):
        try:
            # post data and get request body
            request = requests.post(url + "/predict",data={'a':ANIMAL,'b':AREA,'c':SYMPTOM1,'d':SYMPTOM2}).text

            # strip the request body
            request = request[request.index("<h2>  </h2>")+25:request.index("<br><br>")-19]
            result = request.replace("</h2>","").strip().split("<h2>")
            result = [line.strip("\n ") for line in result]

            message = "강아지의" if ANIMAL.find("강아지") != -1 or ANIMAL.find("개") != -1 else "고양이의"
            if len(AREA) >= 1 and AREA != " ":
                message += (" "+str(AREA))
            if len(SYMPTOM1) >= 1 and SYMPTOM1 != " ":
                message += (" "+str(SYMPTOM1))
            if len(SYMPTOM2) >= 1 and SYMPTOM2 != " ":
                message += (" "+str(SYMPTOM2))
            message += "와(과) 관련된 질병과 그 확률은 다음과 같습니다.\n"

            for i in range(len(result)):
                if i % 2 == 0:
                    message += ("\n" + result[i])
                else:
                    message += ("\t" + str(round(float(result[i].strip()),2)) + "%")
            return message

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
