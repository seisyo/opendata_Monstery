import requests
from bs4 import BeautifulSoup
import json

response = requests.get("http://stpc00601.taipower.com.tw/loadGraph/loadGraph/data/loadareas.csv")
datas = [] ##從csv中抓到的資料
datas = response.content.decode("utf-8").split("\n")
temp = []
result = []

for data in datas:
    temp = data.strip('\r').split(",")
    if temp[0] == '' :    
        break
    else:
        result.append({
            'east':float(temp[1]),
            'south':float(temp[2]),
            'central':float(temp[3]),
            'north':float(temp[4]),
            'per_east':round(float(temp[1])/55.7162, 4),
            'per_south':round(float(temp[2])/630.5750, 4),
            'per_central':round(float(temp[3])/579.9473, 4),
            'per_north':round(float(temp[4])/1054.0288, 4),
            'remain_east':round((923+952-float(temp[1]))/(923+952), 2),
            'remain_south':round((923-float(temp[2]))/923, 2),
            'remain_central':round((952-float(temp[3]))/952, 2),
            'remain_north':round((1010-float(temp[4]))/1010, 2)

            })
print(result[-1])
json_output = json.dumps(result)
print(json_output)