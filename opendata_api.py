from flask import Flask, request, json
from flask_restful import Resource, Api

import requests
# import json

app = Flask(__name__)
api = Api(app)

info = {}
class powerData(Resource):
    def get(self):
        info  = {'region':request.values['region']}

        response = requests.get("http://stpc00601.taipower.com.tw/loadGraph/loadGraph/data/loadareas.csv")
        datas = [] ##從csv中抓到的資料
        datas = response.content.decode("utf-8").split("\n")
        temp = []
        result = []
        results =[]
        region = int(info['region'].replace("north","4").replace("central","3").replace("south","2").replace("east","1"))
        
        for data in datas:
            temp = data.strip('\r').split(",")
            if temp[0] == '' :    
                break   
            else:
                if region == 1:
                    result.append({
                        'time':temp[0],
                        'region':float(temp[region]),
                        'per_region':round(float(temp[1])/55.7162, 4),
                        'remain_region':round((923+952-float(temp[1]))/(923+952), 4)
                        })
                elif region == 2:
                    result.append({
                        'time':temp[0],
                        'region':float(temp[region]),
                        'per_region':round(float(temp[2])/630.5750, 4),
                        'remain_region':round((923-float(temp[2]))/923, 4)
                        })
                elif region == 3:
                    result.append({
                        'time':temp[0],
                        'region':float(temp[region]),
                        'per_region':round(float(temp[3])/579.9473, 4),
                        'remain_region':round((952-float(temp[3]))/952, 4)
                        })
                elif region == 4:
                    result.append({
                        'time':temp[0],
                        'region':float(temp[region]),
                        'per_region':round(float(temp[4])/1054.0288, 4),
                        'remain_region':round((1010-float(temp[4]))/1010, 4)
                        })
                else:
                    break
        results.append({
            'now':result[-1],
            'history':result
            })
        # json_output = json.dumps(results)
        return(json.jsonify({'data': results}))



api.add_resource(powerData, '/powerdata')
if __name__ == '__main__':
    app.run(debug=True)